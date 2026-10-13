"""
Vivaak / Vaza AI Growth System V3.1
Canonical Schema Validator & Integrity Checker

Validates JSON records against schemas in schemas/v3_1/ without external dependencies.
Conforms to JSON Schema Draft 2020-12 basic validation specifications.
"""

import json
import os
import re
from datetime import datetime

SCHEMA_DIR = os.path.dirname(os.path.abspath(__file__))

ISO8601_DATETIME_RE = re.compile(
    r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})$'
)
ISO8601_DATE_RE = re.compile(r'^\d{4}-\d{2}-\d{2}$')

class SchemaValidationError(Exception):
    pass

class SchemaValidator:
    def __init__(self, schema_dir=SCHEMA_DIR):
        self.schema_dir = schema_dir
        self.schemas = {}
        self._load_all_schemas()

    def _load_all_schemas(self):
        for fname in os.listdir(self.schema_dir):
            if fname.endswith(".json") and not fname.startswith("."):
                schema_name = fname[:-5]
                filepath = os.path.join(self.schema_dir, fname)
                with open(filepath, "r", encoding="utf-8") as f:
                    self.schemas[schema_name] = json.load(f)

    def get_schema(self, schema_name):
        canonical_name = schema_name.lower().replace("-", "_")
        if canonical_name in self.schemas:
            return self.schemas[canonical_name]
        raise ValueError(f"Schema '{schema_name}' not found in {self.schema_dir}. Available: {list(self.schemas.keys())}")

    def validate_record(self, schema_name, record):
        schema = self.get_schema(schema_name)
        errors = []

        # 1. Check required fields
        required_fields = schema.get("required", [])
        for field in required_fields:
            if field not in record:
                errors.append(f"Missing required field: '{field}'")
            elif record[field] is None:
                prop_spec = schema.get("properties", {}).get(field, {})
                allowed_types = prop_spec.get("type", [])
                if isinstance(allowed_types, str):
                    allowed_types = [allowed_types]
                if "null" not in allowed_types:
                    errors.append(f"Required field '{field}' cannot be null")

        # 2. Check property types & constraints
        properties = schema.get("properties", {})
        for field, value in record.items():
            if field not in properties:
                # additional properties allowed
                continue
            prop_spec = properties[field]
            field_errors = self._validate_field(field, value, prop_spec)
            errors.extend(field_errors)

        if errors:
            raise SchemaValidationError(f"Validation failed for schema '{schema_name}':\n" + "\n".join(f"  - {e}" for e in errors))

        return True

    def _validate_field(self, field_name, value, prop_spec):
        errors = []
        expected_type = prop_spec.get("type")

        # Handle null values
        if value is None:
            if isinstance(expected_type, list) and "null" in expected_type:
                return []
            elif expected_type == "null":
                return []
            else:
                errors.append(f"Field '{field_name}' is null but schema expects {expected_type}")
                return errors

        # Normalize expected_type into list of allowed types
        if isinstance(expected_type, str):
            allowed_types = [expected_type]
        elif isinstance(expected_type, list):
            allowed_types = expected_type
        else:
            allowed_types = []

        # Type checks
        type_valid = False
        for t in allowed_types:
            if t == "string" and isinstance(value, str):
                type_valid = True
                break
            elif t == "integer" and isinstance(value, int) and not isinstance(value, bool):
                type_valid = True
                break
            elif t == "number" and isinstance(value, (int, float)) and not isinstance(value, bool):
                type_valid = True
                break
            elif t == "boolean" and isinstance(value, bool):
                type_valid = True
                break
            elif t == "array" and isinstance(value, list):
                type_valid = True
                break
            elif t == "object" and isinstance(value, dict):
                type_valid = True
                break

        if not type_valid and allowed_types:
            errors.append(f"Field '{field_name}' has value '{value}' ({type(value).__name__}) which does not match expected type {expected_type}")
            return errors

        # Enum check
        if "enum" in prop_spec:
            allowed_enums = prop_spec["enum"]
            if value not in allowed_enums:
                errors.append(f"Field '{field_name}' has value '{value}' which is not in allowed enums: {allowed_enums}")

        # Format checks
        format_spec = prop_spec.get("format")
        if format_spec and isinstance(value, str):
            if format_spec == "date-time":
                if not ISO8601_DATETIME_RE.match(value):
                    errors.append(f"Field '{field_name}' with value '{value}' is not a valid ISO 8601 date-time string (e.g. 2026-10-05T12:00:00+05:30)")
            elif format_spec == "date":
                if not ISO8601_DATE_RE.match(value):
                    errors.append(f"Field '{field_name}' with value '{value}' is not a valid ISO 8601 date string (YYYY-MM-DD)")
            elif format_spec == "uri":
                if not (value.startswith("http://") or value.startswith("https://")):
                    errors.append(f"Field '{field_name}' with value '{value}' must be an absolute URI starting with http:// or https://")

        # Range checks
        if "minimum" in prop_spec and isinstance(value, (int, float)):
            if value < prop_spec["minimum"]:
                errors.append(f"Field '{field_name}' value {value} is less than minimum {prop_spec['minimum']}")
        if "maximum" in prop_spec and isinstance(value, (int, float)):
            if value > prop_spec["maximum"]:
                errors.append(f"Field '{field_name}' value {value} is greater than maximum {prop_spec['maximum']}")

        return errors


def test_validator():
    validator = SchemaValidator()
    print(f"Loaded {len(validator.schemas)} schemas into validator.")

    # Test Sample 1: Property Record
    vaza_property = {
        "property_id": "PROP-VAZA-001",
        "brand_id": "ENT-BRAND-VIVAAK",
        "name": "Vaza Villa",
        "canonical_name": "Vaza Luxury Villa Barog",
        "property_type": "VILLA",
        "description": "Ultra-luxury 4-bedroom private estate in Barog, Himachal Pradesh featuring private heated jacuzzi, plunge pool, and panoramic Himalayan vistas.",
        "location_id": "LOC-BAROG-001",
        "address": "Barog Heights, Kumarhatti-Barog Road, Solan District, Himachal Pradesh 173211",
        "latitude": 30.8924,
        "longitude": 77.0833,
        "bedrooms": 4,
        "bathrooms": 5,
        "guest_capacity": 12,
        "amenities": ["AMEN-POOL-001", "AMEN-JACUZZI-001", "AMEN-CHEF-001"],
        "experiences": ["EXP-FAMILY-001", "EXP-WEEKEND-001"],
        "ideal_for": ["Luxury Family Stays", "Private Group Retreats", "Milestone Celebrations"],
        "booking_methods": ["Direct Website", "Concierge WhatsApp", "Phone"],
        "official_url": "https://vivaak.com/vaza-villa/",
        "image_urls": ["https://pub-b06262d1d441495c8cb4dfbe908bdae7.r2.dev/vaza-pool.jpg"],
        "verified_claims": ["CLAIM-HEATED-JACUZZI", "CLAIM-FOUR-BEDROOMS"],
        "status": "ACTIVE",
        "last_verified_at": "2026-10-05T12:00:00+05:30"
    }

    try:
        validator.validate_record("property", vaza_property)
        print(" Test 1 (Property schema): PASSED")
    except SchemaValidationError as e:
        print(f"❌ Test 1 (Property schema) FAILED: {e}")

    # Test Sample 2: GSC Query Record
    gsc_sample = {
        "record_id": "GSC-20261005-001",
        "date": "2026-10-04",
        "query": "luxury villa in barog himachal",
        "page_url": "https://vivaak.com/vaza-villa/",
        "country": "ind",
        "device": "MOBILE",
        "search_appearance": None,
        "clicks": 14,
        "impressions": 180,
        "ctr": 0.0778,
        "position": 6.2,
        "source": "GSC",
        "retrieved_at": "2026-10-05T06:00:00+05:30",
        "striking_distance": True,
        "high_impression_low_ctr": False,
        "ranking_decline": False,
        "traffic_growth": True,
        "new_query": False,
        "cannibalization_signal": False,
        "commercial_opportunity": True
    }

    try:
        validator.validate_record("gsc_query", gsc_sample)
        print(" Test 2 (GSC Query schema): PASSED")
    except SchemaValidationError as e:
        print(f"❌ Test 2 (GSC Query schema) FAILED: {e}")

    # Test Sample 3: Strategic State Record
    strategy_state_sample = {
        "state_id": "STATE-20261005",
        "date": "2026-10-05",
        "current_phase": "EXECUTION_PHASE_1",
        "north_star": {
            "target_quarter": "Q4-2026",
            "target_inquiries": 150,
            "current_inquiries": 28,
            "focus_markets": ["Delhi NCR", "Chandigarh Tricity", "Punjab"],
            "focus_entities": ["The Vivaak Villa", "Vaza Villa"]
        },
        "top_priorities": [
            "ACT-001 Live Verification & Indexing",
            "Vaza Barog Core Commercial Terms",
            "Striking-distance queries (Pos 4-20)"
        ],
        "top_opportunities": [
            "Capture 'luxury villa in barog' page-one rank",
            "Expand AEO answer capsules on FAQ page"
        ],
        "top_risks": [
            "OTA keyword dominance on unbranded destination queries"
        ],
        "active_experiments": ["EXP-001", "EXP-002"],
        "recent_learnings": [
            "Pre-rendered SSR H1s drastically improve indexing velocity compared to client-side RTDB hydration"
        ],
        "forecast_summary": {
            "30_day_organic_clicks": 320,
            "page_one_keywords": 8
        },
        "competitor_summary": None,
        "ai_visibility_summary": None,
        "next_best_action": {
            "action_id": "NBA-20261005-001",
            "date": "2026-10-05",
            "action": "Deploy V3.1 Canonical Schemas across all 21 agents and state memory",
            "page_id": "SITE_WIDE",
            "reason": "Ensure uniform data contract across Swarm Layer 1 to 5",
            "evidence": "V3.1 Data Architecture requirement",
            "expected_impact": "HIGH",
            "effort": "LOW",
            "confidence": "HIGH",
            "owner": "Archivist",
            "approval_required": "LEVEL_B",
            "deadline": "2026-10-05T18:00:00+05:30",
            "status": "IN_PROGRESS"
        },
        "reason": "Transitioning system memory to canonical V3.1 schema specification",
        "updated_by": "Conductor"
    }

    try:
        validator.validate_record("strategy_state", strategy_state_sample)
        print(" Test 3 (Strategy State schema): PASSED")
    except SchemaValidationError as e:
        print(f"❌ Test 3 (Strategy State schema) FAILED: {e}")

if __name__ == "__main__":
    test_validator()
