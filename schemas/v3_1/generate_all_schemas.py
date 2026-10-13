"""
Vivaak / Vaza AI Growth System V3.1
Machine-Readable JSON Schema Generator (Conforms to JSON Schema Draft 2020-12)
"""

import json
import os

SCHEMA_DIR = os.path.dirname(os.path.abspath(__file__))

def create_schema(title, description, properties, required=None):
    schema = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": f"https://vivaak.com/schemas/v3_1/{title.lower().replace(' ', '_')}.json",
        "title": title,
        "description": description,
        "type": "object",
        "properties": properties,
        "additionalProperties": True
    }
    if required:
        schema["required"] = required
    return schema

UNIVERSAL_METADATA_PROPERTIES = {
    "id": {"type": "string", "description": "Unique persistent identifier."},
    "record_type": {"type": "string", "description": "Canonical object type."},
    "created_at": {"type": "string", "format": "date-time", "description": "Creation timestamp in ISO 8601."},
    "updated_at": {"type": "string", "format": "date-time", "description": "Last modification timestamp in ISO 8601."},
    "source": {
        "type": "string",
        "enum": ["DATAFORSEO", "GSC", "GA4", "GTM", "FIRECRAWL", "WEBSITE_REPOSITORY", "VIVAAK_KNOWLEDGE_BASE", "HUMAN", "AGENT"],
        "description": "Originating source system."
    },
    "source_id": {"type": ["string", "null"], "description": "Identifier supplied by source if available."},
    "source_timestamp": {"type": ["string", "null"], "format": "date-time", "description": "When source record was retrieved."},
    "status": {
        "type": "string",
        "enum": ["ACTIVE", "DRAFT", "PENDING_REVIEW", "APPROVED", "IMPLEMENTED", "ARCHIVED", "REJECTED", "UNKNOWN"],
        "description": "Current lifecycle status."
    },
    "confidence": {
        "type": ["string", "null"],
        "enum": ["HIGH", "MEDIUM", "LOW", "UNKNOWN", None],
        "description": "Confidence level of record."
    },
    "notes": {"type": ["string", "null"], "description": "Contextual operational remarks."}
}

SCHEMAS = {
    "universal_record_metadata": create_schema(
        "Universal Record Metadata",
        "Universal metadata fields required on all persistent system records.",
        UNIVERSAL_METADATA_PROPERTIES,
        required=["id", "record_type", "created_at", "updated_at", "source", "status"]
    ),

    "entity": create_schema(
        "Entity",
        "Canonical business, physical, or conceptual entity in the Vivaak / Vaza ecosystem.",
        {
            "entity_id": {"type": "string", "description": "Unique entity identifier."},
            "entity_type": {
                "type": "string",
                "enum": ["BRAND", "PROPERTY", "LOCATION", "DESTINATION", "AMENITY", "EXPERIENCE", "SERVICE", "EVENT", "FOOD", "ATTRACTION", "PERSON", "ORGANIZATION", "CONCEPT", "QUERY_TOPIC"],
                "description": "Canonical entity classification."
            },
            "name": {"type": "string", "description": "Display name."},
            "canonical_name": {"type": "string", "description": "Unique standardized entity name."},
            "description": {"type": ["string", "null"], "description": "Detailed entity description."},
            "parent_entity_id": {"type": ["string", "null"], "description": "Reference to parent entity ID."},
            "aliases": {"type": "array", "items": {"type": "string"}, "description": "Known entity aliases."},
            "location": {"type": ["string", "null"], "description": "Geographical location context."},
            "properties": {"type": ["object", "null"], "description": "Dynamic attribute key-value pairs."},
            "source": {"type": "string", "description": "Originating source of entity record."},
            "verified": {"type": "boolean", "description": "Whether entity has been verified."},
            "verification_status": {
                "type": "string",
                "enum": ["VERIFIED", "PARTIALLY_VERIFIED", "UNVERIFIED", "CONFLICTING", "UNKNOWN"],
                "description": "Strict verification state."
            },
            "created_at": {"type": "string", "format": "date-time"},
            "updated_at": {"type": "string", "format": "date-time"}
        },
        required=["entity_id", "entity_type", "name", "canonical_name", "source", "verified", "verification_status", "created_at", "updated_at"]
    ),

    "property": create_schema(
        "Property",
        "Luxury stay or estate property entity (The Vivaak Villa, Vaza Villa, etc.).",
        {
            "property_id": {"type": "string", "description": "Unique property identifier."},
            "brand_id": {"type": "string", "description": "Reference to parent brand entity_id (e.g., ENT-BRAND-VIVAAK)."},
            "name": {"type": "string", "description": "Property name."},
            "canonical_name": {"type": "string", "description": "Canonical property name."},
            "property_type": {
                "type": "string",
                "enum": ["VILLA", "HOTEL", "RESORT", "HOMESTAY", "RETREAT", "OTHER"],
                "description": "Property category."
            },
            "description": {"type": "string", "description": "Detailed verified narrative of property."},
            "location_id": {"type": "string", "description": "Foreign key reference to LOCATION schema."},
            "address": {"type": "string", "description": "Physical address."},
            "latitude": {"type": "number", "description": "Geographic latitude coordinate."},
            "longitude": {"type": "number", "description": "Geographic longitude coordinate."},
            "bedrooms": {"type": "integer", "minimum": 1, "description": "Verified bedroom count."},
            "bathrooms": {"type": "integer", "minimum": 1, "description": "Verified bathroom count."},
            "guest_capacity": {"type": "integer", "minimum": 1, "description": "Maximum comfortable guest capacity."},
            "amenities": {"type": "array", "items": {"type": "string"}, "description": "Array of AMENITY IDs."},
            "experiences": {"type": "array", "items": {"type": "string"}, "description": "Array of EXPERIENCE IDs."},
            "ideal_for": {"type": "array", "items": {"type": "string"}, "description": "Target traveler/stay personas."},
            "booking_methods": {"type": "array", "items": {"type": "string"}, "description": "Available booking pathways."},
            "official_url": {"type": "string", "format": "uri", "description": "Canonical absolute URL."},
            "image_urls": {"type": "array", "items": {"type": "string", "format": "uri"}, "description": "High-res CDN image URLs."},
            "verified_claims": {"type": "array", "items": {"type": "string"}, "description": "Array of CLAIM IDs."},
            "status": {"type": "string", "enum": ["ACTIVE", "INACTIVE", "DRAFT"]},
            "last_verified_at": {"type": "string", "format": "date-time"}
        },
        required=["property_id", "brand_id", "name", "canonical_name", "property_type", "description", "location_id", "address", "latitude", "longitude", "bedrooms", "bathrooms", "guest_capacity", "official_url", "status", "last_verified_at"]
    ),

    "location": create_schema(
        "Location",
        "Geographic entity representing destination, town, valley, or landmark.",
        {
            "location_id": {"type": "string", "description": "Unique location identifier."},
            "name": {"type": "string", "description": "Geographic name."},
            "location_type": {
                "type": "string",
                "enum": ["COUNTRY", "STATE", "DISTRICT", "CITY", "TOWN", "LOCALITY", "DESTINATION", "ATTRACTION", "LANDMARK", "REGION"]
            },
            "parent_location_id": {"type": ["string", "null"], "description": "Parent location reference."},
            "country": {"type": "string", "description": "Country name."},
            "state": {"type": "string", "description": "State or province."},
            "district": {"type": ["string", "null"], "description": "District."},
            "city": {"type": ["string", "null"], "description": "City or municipality."},
            "locality": {"type": ["string", "null"], "description": "Specific locality or village."},
            "latitude": {"type": ["number", "null"], "description": "Latitude coordinate."},
            "longitude": {"type": ["number", "null"], "description": "Longitude coordinate."},
            "aliases": {"type": "array", "items": {"type": "string"}},
            "description": {"type": ["string", "null"]},
            "verified": {"type": "boolean"},
            "source": {"type": "string"},
            "last_verified_at": {"type": "string", "format": "date-time"}
        },
        required=["location_id", "name", "location_type", "country", "state", "verified", "source", "last_verified_at"]
    ),

    "amenity": create_schema(
        "Amenity",
        "Physical amenity or luxury facility offered at a Vivaak / Vaza property.",
        {
            "amenity_id": {"type": "string"},
            "property_id": {"type": "string", "description": "Foreign key reference to PROPERTY schema."},
            "name": {"type": "string"},
            "canonical_name": {"type": "string"},
            "description": {"type": "string"},
            "category": {
                "type": "string",
                "enum": ["POOL", "JACUZZI", "DINING", "ROOM", "ENTERTAINMENT", "OUTDOOR", "WELLNESS", "FAMILY", "PET", "EVENT", "SERVICE", "OTHER"]
            },
            "availability": {
                "type": "string",
                "enum": ["AVAILABLE", "SEASONAL", "ON_REQUEST", "UNAVAILABLE", "UNKNOWN"]
            },
            "verified": {"type": "boolean"},
            "source": {"type": "string"},
            "last_verified_at": {"type": "string", "format": "date-time"},
            "related_queries": {"type": "array", "items": {"type": "string"}}
        },
        required=["amenity_id", "property_id", "name", "canonical_name", "description", "category", "availability", "verified", "source", "last_verified_at"]
    ),

    "experience": create_schema(
        "Experience",
        "Curated stay, dining, or celebration experience provided by Vivaak / Vaza.",
        {
            "experience_id": {"type": "string"},
            "property_id": {"type": "string", "description": "Foreign key reference to PROPERTY schema."},
            "name": {"type": "string"},
            "experience_type": {
                "type": "string",
                "enum": ["FAMILY_STAY", "GROUP_STAY", "BIRTHDAY", "CELEBRATION", "CORPORATE", "EVENT", "DINING", "WEEKEND_GETAWAY", "SEASONAL", "LOCAL_EXPERIENCE", "OTHER"]
            },
            "description": {"type": "string"},
            "audience": {"type": "array", "items": {"type": "string"}},
            "seasonality": {"type": ["string", "null"]},
            "availability": {
                "type": "string",
                "enum": ["AVAILABLE", "SEASONAL", "ON_REQUEST", "UNAVAILABLE", "UNKNOWN"]
            },
            "booking_required": {"type": "boolean"},
            "verified": {"type": "boolean"},
            "source": {"type": "string"},
            "related_queries": {"type": "array", "items": {"type": "string"}},
            "landing_page_url": {"type": ["string", "null"], "format": "uri"}
        },
        required=["experience_id", "property_id", "name", "experience_type", "description", "availability", "booking_required", "verified", "source"]
    ),

    "page": create_schema(
        "Page",
        "Individual page route within the Vivaak / Vaza web architecture.",
        {
            "page_id": {"type": "string"},
            "url": {"type": "string", "format": "uri"},
            "canonical_url": {"type": "string", "format": "uri"},
            "route": {"type": "string"},
            "page_type": {
                "type": "string",
                "enum": ["HOME", "PROPERTY", "LOCATION", "AMENITY", "EXPERIENCE", "EVENT", "DESTINATION", "LOCAL_GUIDE", "FOOD", "FAQ", "JOURNAL", "BLOG", "COMMERCIAL", "REFERENCE", "LEGAL", "SUPPORT", "OTHER"]
            },
            "property_id": {"type": ["string", "null"]},
            "location_id": {"type": ["string", "null"]},
            "title": {"type": "string"},
            "meta_description": {"type": "string"},
            "h1": {"type": "string"},
            "h2s": {"type": "array", "items": {"type": "string"}},
            "h3s": {"type": "array", "items": {"type": "string"}},
            "body_text": {"type": "string"},
            "word_count": {"type": "integer", "minimum": 0},
            "language": {"type": "string", "default": "en-IN"},
            "indexability": {
                "type": "string",
                "enum": ["INDEXABLE", "NOINDEX", "REDIRECT", "BLOCKED"]
            },
            "canonical_status": {
                "type": "string",
                "enum": ["CANONICAL_SELF", "CANONICAL_POINTS_TO_OTHER", "DUPLICATE_CANONICAL", "MISSING"]
            },
            "robots_directive": {"type": "string"},
            "status_code": {"type": "integer"},
            "content_source": {"type": "string"},
            "content_version": {"type": "string"},
            "first_published_at": {"type": ["string", "null"], "format": "date-time"},
            "last_modified_at": {"type": "string", "format": "date-time"},
            "last_crawled_at": {"type": "string", "format": "date-time"},
            "target_keyword_id": {"type": ["string", "null"]},
            "secondary_keyword_ids": {"type": "array", "items": {"type": "string"}},
            "search_intent": {
                "type": "string",
                "enum": ["NAVIGATIONAL", "INFORMATIONAL", "COMMERCIAL_INVESTIGATION", "TRANSACTIONAL", "LOCAL", "DESTINATION", "PROPERTY", "EXPERIENCE", "BOOKING"]
            },
            "commercial_intent": {
                "type": "string",
                "enum": ["VERY_HIGH", "HIGH", "MEDIUM", "LOW", "NONE", "UNKNOWN"]
            },
            "conversion_intent": {
                "type": "string",
                "enum": ["DIRECT_BOOKING", "WHATSAPP_ENQUIRY", "PHONE_CALL", "LEAD_FORM", "INFORMATIONAL_DISCOVERY"]
            },
            "schema_types": {"type": "array", "items": {"type": "string"}},
            "internal_links": {"type": "array", "items": {"type": "object"}},
            "external_links": {"type": "array", "items": {"type": "object"}},
            "image_count": {"type": "integer", "minimum": 0},
            "image_alt_coverage": {"type": "number", "minimum": 0.0, "maximum": 1.0},
            "content_quality": {
                "type": "string",
                "enum": ["EXCELLENT", "STRONG", "GOOD", "PARTIAL", "WEAK", "UNKNOWN"]
            },
            "ai_sourceability": {
                "type": "string",
                "enum": ["EXCELLENT", "STRONG", "GOOD", "PARTIAL", "WEAK", "UNKNOWN"]
            },
            "recommended_action": {
                "type": "string",
                "enum": ["KEEP", "OPTIMIZE", "REWRITE", "EXPAND", "CONSOLIDATE", "REDIRECT", "NOINDEX", "PROTECTED", "DO_NOT_TOUCH"]
            },
            "priority": {"type": "string", "enum": ["P0", "P1", "P2", "P3", "P4"]},
            "owner": {"type": "string"},
            "verification_status": {
                "type": "string",
                "enum": ["VERIFIED", "PENDING_REVIEW", "REVISION_REQUIRED"]
            }
        },
        required=[
            "page_id", "url", "canonical_url", "route", "page_type", "title",
            "meta_description", "h1", "body_text", "word_count", "language",
            "indexability", "canonical_status", "robots_directive", "status_code",
            "content_source", "content_version", "last_modified_at", "last_crawled_at",
            "search_intent", "commercial_intent", "conversion_intent", "priority",
            "owner", "verification_status"
        ]
    ),

    "keyword": create_schema(
        "Keyword",
        "Target search query, intent classification, volume, and ranking telemetry.",
        {
            "keyword_id": {"type": "string"},
            "keyword": {"type": "string"},
            "normalized_keyword": {"type": "string"},
            "language": {"type": "string", "default": "en"},
            "country": {"type": "string", "default": "in"},
            "location": {"type": ["string", "null"]},
            "device": {"type": "string", "enum": ["DESKTOP", "MOBILE", "TABLET", "ALL"]},
            "search_engine": {"type": "string", "enum": ["GOOGLE", "BING", "ALL"]},
            "keyword_type": {
                "type": "string",
                "enum": ["CORE", "DISCOVERED", "GSC", "COMPETITOR", "PAA", "RELATED", "LONG_TAIL", "BUYER_LANGUAGE", "LOCAL", "SEASONAL", "AI_DISCOVERED", "BRANDED", "NON_BRANDED"]
            },
            "search_intent": {
                "type": "string",
                "enum": ["NAVIGATIONAL", "INFORMATIONAL", "COMMERCIAL_INVESTIGATION", "TRANSACTIONAL", "LOCAL", "DESTINATION", "PROPERTY", "EXPERIENCE", "BOOKING"]
            },
            "commercial_intent": {
                "type": "string",
                "enum": ["VERY_HIGH", "HIGH", "MEDIUM", "LOW", "NONE", "UNKNOWN"]
            },
            "business_relevance": {
                "type": "string",
                "enum": ["HIGH", "MEDIUM", "LOW", "NONE"]
            },
            "property_relevance": {"type": "array", "items": {"type": "string"}},
            "search_volume": {"type": ["integer", "null"]},
            "search_volume_source": {"type": ["string", "null"]},
            "cpc": {"type": ["number", "null"]},
            "competition": {"type": ["number", "null"]},
            "trend_direction": {"type": ["string", "null"], "enum": ["RISING", "STABLE", "DECLINING", "UNKNOWN", None]},
            "trend_source": {"type": ["string", "null"]},
            "current_target_page_id": {"type": ["string", "null"]},
            "recommended_target_page_id": {"type": ["string", "null"]},
            "current_position": {"type": ["number", "null"]},
            "best_position": {"type": ["number", "null"]},
            "impressions": {"type": ["integer", "null"]},
            "clicks": {"type": ["integer", "null"]},
            "ctr": {"type": ["number", "null"]},
            "conversion_count": {"type": ["integer", "null"]},
            "ai_relevance": {"type": "string", "enum": ["HIGH", "MEDIUM", "LOW", "UNKNOWN"]},
            "priority": {"type": "string", "enum": ["P0", "P1", "P2", "P3", "P4"]},
            "opportunity_score": {"type": ["number", "null"]},
            "last_updated_at": {"type": "string", "format": "date-time"}
        },
        required=["keyword_id", "keyword", "normalized_keyword", "language", "country", "device", "search_engine", "keyword_type", "search_intent", "commercial_intent", "business_relevance", "ai_relevance", "priority", "last_updated_at"]
    ),

    "serp_snapshot": create_schema(
        "SERP Snapshot",
        "Point-in-time capture of complete SERP for a target query and location.",
        {
            "serp_snapshot_id": {"type": "string"},
            "keyword": {"type": "string"},
            "keyword_id": {"type": "string"},
            "search_engine": {"type": "string"},
            "country": {"type": "string"},
            "location": {"type": "string"},
            "language": {"type": "string"},
            "device": {"type": "string"},
            "search_type": {"type": "string"},
            "retrieved_at": {"type": "string", "format": "date-time"},
            "results": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "position": {"type": "integer"},
                        "url": {"type": "string", "format": "uri"},
                        "domain": {"type": "string"},
                        "title": {"type": "string"},
                        "description": {"type": ["string", "null"]},
                        "breadcrumb": {"type": ["string", "null"]},
                        "result_type": {"type": "string"},
                        "featured_snippet": {"type": "boolean"},
                        "domain_rank": {"type": ["number", "null"]},
                        "page_type": {"type": ["string", "null"]}
                    },
                    "required": ["position", "url", "domain", "title"]
                }
            },
            "serp_features": {"type": "array", "items": {"type": "object"}},
            "paa_questions": {"type": "array", "items": {"type": "object"}},
            "related_searches": {"type": "array", "items": {"type": "string"}},
            "ai_features": {
                "type": ["object", "null"],
                "properties": {
                    "ai_overview_present": {"type": "boolean"},
                    "ai_mode_present": {"type": "boolean"},
                    "sources": {"type": "array", "items": {"type": "string", "format": "uri"}}
                }
            },
            "local_results": {"type": "array", "items": {"type": "object"}},
            "knowledge_graph": {"type": ["object", "null"]},
            "organic_result_count": {"type": "integer"}
        },
        required=["serp_snapshot_id", "keyword", "keyword_id", "search_engine", "country", "location", "language", "device", "retrieved_at", "results", "organic_result_count"]
    ),

    "paa_question": create_schema(
        "PAA Question",
        "People Also Ask question extracted from SERP for AEO targeting.",
        {
            "paa_id": {"type": "string"},
            "keyword_id": {"type": "string"},
            "question": {"type": "string"},
            "normalized_question": {"type": "string"},
            "language": {"type": "string"},
            "country": {"type": "string"},
            "location": {"type": ["string", "null"]},
            "source_serp_id": {"type": "string"},
            "position": {"type": "integer"},
            "parent_question_id": {"type": ["string", "null"]},
            "intent": {"type": "string"},
            "mapped_page_id": {"type": ["string", "null"]},
            "recommended_content_location": {
                "type": "string",
                "enum": ["H2", "H3", "FAQ", "BODY", "EXISTING_PAGE", "NEW_PAGE", "DO_NOT_TARGET"]
            },
            "status": {
                "type": "string",
                "enum": ["IDENTIFIED", "MAPPED", "IMPLEMENTED", "DISMISSED"]
            },
            "first_seen": {"type": "string", "format": "date-time"},
            "last_seen": {"type": "string", "format": "date-time"}
        },
        required=["paa_id", "keyword_id", "question", "normalized_question", "language", "country", "source_serp_id", "position", "intent", "recommended_content_location", "status", "first_seen", "last_seen"]
    ),

    "gsc_query": create_schema(
        "GSC Query Record",
        "Google Search Console query observation with immutable raw and calculated derived fields.",
        {
            "record_id": {"type": "string"},
            "date": {"type": "string", "format": "date"},
            "query": {"type": "string"},
            "page_url": {"type": "string", "format": "uri"},
            "country": {"type": "string"},
            "device": {"type": "string"},
            "search_appearance": {"type": ["string", "null"]},
            "clicks": {"type": "integer", "minimum": 0},
            "impressions": {"type": "integer", "minimum": 0},
            "ctr": {"type": "number", "minimum": 0.0, "maximum": 1.0},
            "position": {"type": "number", "minimum": 1.0},
            "source": {"type": "string", "default": "GSC"},
            "retrieved_at": {"type": "string", "format": "date-time"},
            "striking_distance": {"type": "boolean", "description": "Derived: position >= 4.0 and position <= 20.0"},
            "high_impression_low_ctr": {"type": "boolean", "description": "Derived: impressions >= 50 and ctr <= 0.02"},
            "ranking_decline": {"type": "boolean"},
            "traffic_growth": {"type": "boolean"},
            "new_query": {"type": "boolean"},
            "cannibalization_signal": {"type": "boolean"},
            "commercial_opportunity": {"type": "boolean"}
        },
        required=["record_id", "date", "query", "page_url", "country", "device", "clicks", "impressions", "ctr", "position", "source", "retrieved_at"]
    ),

    "ga4_landing_page": create_schema(
        "GA4 Landing Page Record",
        "Google Analytics 4 traffic, engagement, and conversion observation.",
        {
            "date": {"type": "string", "format": "date"},
            "landing_page": {"type": "string", "format": "uri"},
            "source": {"type": "string"},
            "medium": {"type": "string"},
            "campaign": {"type": ["string", "null"]},
            "users": {"type": "integer", "minimum": 0},
            "sessions": {"type": "integer", "minimum": 0},
            "engaged_sessions": {"type": "integer", "minimum": 0},
            "engagement_rate": {"type": "number", "minimum": 0.0, "maximum": 1.0},
            "conversions": {"type": "integer", "minimum": 0},
            "key_events": {"type": "integer", "minimum": 0},
            "booking_events": {"type": "integer", "minimum": 0},
            "whatsapp_events": {"type": "integer", "minimum": 0},
            "phone_events": {"type": "integer", "minimum": 0},
            "form_events": {"type": "integer", "minimum": 0},
            "revenue": {"type": ["number", "null"], "description": "Strictly null if PMS is unintegrated."},
            "country": {"type": "string"},
            "device": {"type": "string"},
            "retrieved_at": {"type": "string", "format": "date-time"}
        },
        required=["date", "landing_page", "source", "medium", "users", "sessions", "engaged_sessions", "engagement_rate", "conversions", "key_events", "booking_events", "whatsapp_events", "phone_events", "form_events", "country", "device", "retrieved_at"]
    ),

    "tracking_event": create_schema(
        "Tracking Event",
        "Google Tag Manager event definition and conversion telemetry.",
        {
            "event_id": {"type": "string"},
            "event_name": {"type": "string"},
            "event_type": {
                "type": "string",
                "enum": ["BOOKING", "WHATSAPP", "PHONE", "EMAIL", "FORM", "CTA", "DIRECTIONS", "OUTBOUND", "OTHER"]
            },
            "page_url": {"type": "string", "format": "uri"},
            "element": {"type": ["string", "null"]},
            "event_category": {"type": "string"},
            "event_action": {"type": "string"},
            "event_label": {"type": ["string", "null"]},
            "conversion": {"type": "boolean"},
            "ga4_event_name": {"type": "string"},
            "gtm_container": {"type": "string"},
            "implementation_status": {
                "type": "string",
                "enum": ["ACTIVE", "DRAFT", "TESTING", "INACTIVE"]
            },
            "verification_status": {
                "type": "string",
                "enum": ["VERIFIED", "UNVERIFIED"]
            }
        },
        required=["event_id", "event_name", "event_type", "page_url", "event_category", "event_action", "conversion", "ga4_event_name", "gtm_container", "implementation_status", "verification_status"]
    ),

    "competitor": create_schema(
        "Competitor",
        "Tracked competitor domain, property, or hospitality portal.",
        {
            "competitor_id": {"type": "string"},
            "domain": {"type": "string"},
            "name": {"type": "string"},
            "competitor_type": {
                "type": "string",
                "enum": ["DIRECT_PROPERTY", "LOCAL_HOSPITALITY", "DESTINATION", "TRAVEL_PLATFORM", "OTA", "EDITORIAL", "DIRECTORY", "OTHER"]
            },
            "location": {"type": "string"},
            "market": {"type": "string"},
            "relevance": {"type": "string", "enum": ["HIGH", "MEDIUM", "LOW"]},
            "discovered_by": {"type": "string"},
            "discovery_date": {"type": "string", "format": "date-time"},
            "active": {"type": "boolean"},
            "notes": {"type": ["string", "null"]}
        },
        required=["competitor_id", "domain", "name", "competitor_type", "location", "market", "relevance", "discovered_by", "discovery_date", "active"]
    ),

    "content_gap": create_schema(
        "Content Gap",
        "Identified content, semantic, or entity deficiency on a page.",
        {
            "gap_id": {"type": "string"},
            "page_id": {"type": "string"},
            "gap_type": {
                "type": "string",
                "enum": ["MISSING_TOPIC", "MISSING_QUESTION", "MISSING_ENTITY", "MISSING_FIRST_PARTY_INFORMATION", "MISSING_LOCAL_INFORMATION", "MISSING_INTERNAL_LINK", "MISSING_METADATA", "MISSING_STRUCTURE", "MISSING_FAQ", "MISSING_CONVERSION_PATH", "OUTDATED_INFORMATION", "WEAK_EXPERTISE", "SERP_MISMATCH", "AI_SOURCEABILITY", "OTHER"]
            },
            "description": {"type": "string"},
            "evidence": {"type": "string"},
            "source_records": {"type": "array", "items": {"type": "string"}},
            "competitor_evidence": {"type": "array", "items": {"type": "string"}},
            "search_evidence": {"type": "array", "items": {"type": "string"}},
            "business_value": {"type": "string", "enum": ["HIGH", "MEDIUM", "LOW"]},
            "seo_value": {"type": "number"},
            "aeo_value": {"type": "number"},
            "geo_value": {"type": "number"},
            "commercial_value": {"type": "number"},
            "effort": {"type": "string", "enum": ["LOW", "MEDIUM", "HIGH"]},
            "confidence": {"type": "string", "enum": ["HIGH", "MEDIUM", "LOW", "UNKNOWN"]},
            "priority": {"type": "string", "enum": ["P0", "P1", "P2", "P3", "P4"]},
            "recommended_action": {"type": "string"},
            "status": {"type": "string", "enum": ["OPEN", "IN_PROGRESS", "RESOLVED", "DISMISSED"]}
        },
        required=["gap_id", "page_id", "gap_type", "description", "evidence", "business_value", "seo_value", "aeo_value", "geo_value", "commercial_value", "effort", "confidence", "priority", "recommended_action", "status"]
    ),

    "content_opportunity": create_schema(
        "Content Opportunity",
        "Ranked, actionable growth opportunity combining query, page, and gap data.",
        {
            "opportunity_id": {"type": "string"},
            "page_id": {"type": "string"},
            "keyword_id": {"type": "string"},
            "topic": {"type": "string"},
            "primary_query": {"type": "string"},
            "secondary_queries": {"type": "array", "items": {"type": "string"}},
            "search_intent": {"type": "string"},
            "commercial_intent": {"type": "string"},
            "business_value": {"type": "string", "enum": ["VERY_HIGH", "HIGH", "MEDIUM", "LOW"]},
            "current_rank": {"type": ["number", "null"]},
            "impressions": {"type": ["integer", "null"]},
            "clicks": {"type": ["integer", "null"]},
            "ctr": {"type": ["number", "null"]},
            "conversion_count": {"type": ["integer", "null"]},
            "serp_competition": {"type": "string", "enum": ["LOW", "MEDIUM", "HIGH"]},
            "content_gap_ids": {"type": "array", "items": {"type": "string"}},
            "competitor_gap": {"type": ["string", "null"]},
            "ai_opportunity": {"type": "string", "enum": ["HIGH", "MEDIUM", "LOW"]},
            "local_opportunity": {"type": "string", "enum": ["HIGH", "MEDIUM", "LOW"]},
            "estimated_effort": {"type": "string", "enum": ["LOW", "MEDIUM", "HIGH"]},
            "estimated_impact": {"type": "string", "enum": ["HIGH", "MEDIUM", "LOW"]},
            "confidence": {"type": "string", "enum": ["HIGH", "MEDIUM", "LOW", "UNKNOWN"]},
            "forecast_id": {"type": ["string", "null"]},
            "recommended_action": {
                "type": "string",
                "enum": ["OPTIMIZE", "REWRITE", "EXPAND", "CREATE", "CONSOLIDATE", "REDIRECT", "EXPERIMENT", "DO_NOT_PURSUE"]
            },
            "priority": {"type": "string", "enum": ["P0", "P1", "P2", "P3", "P4"]},
            "owner": {"type": "string"},
            "status": {
                "type": "string",
                "enum": ["IDENTIFIED", "APPROVED", "IN_PROGRESS", "IMPLEMENTED", "ARCHIVED"]
            },
            "created_at": {"type": "string", "format": "date-time"},
            "updated_at": {"type": "string", "format": "date-time"}
        },
        required=["opportunity_id", "page_id", "keyword_id", "topic", "primary_query", "business_value", "serp_competition", "ai_opportunity", "local_opportunity", "estimated_effort", "estimated_impact", "confidence", "recommended_action", "priority", "owner", "status", "created_at", "updated_at"]
    ),

    "content_brief": create_schema(
        "Content Brief",
        "Detailed editorial specification issued by Editor (#20) for Scribe and Tuner.",
        {
            "brief_id": {"type": "string"},
            "page_id": {"type": "string"},
            "opportunity_id": {"type": "string"},
            "primary_keyword": {"type": "string"},
            "secondary_keywords": {"type": "array", "items": {"type": "string"}},
            "search_intent": {"type": "string"},
            "commercial_intent": {"type": "string"},
            "audience": {"type": "string"},
            "page_role": {"type": "string"},
            "recommended_title": {"type": "string"},
            "recommended_meta": {"type": "string"},
            "recommended_h1": {"type": "string"},
            "recommended_h2s": {"type": "array", "items": {"type": "string"}},
            "recommended_h3s": {"type": "array", "items": {"type": "string"}},
            "paa_questions": {"type": "array", "items": {"type": "string"}},
            "entities_to_cover": {"type": "array", "items": {"type": "string"}},
            "first_party_information": {"type": "array", "items": {"type": "string"}},
            "internal_links": {"type": "array", "items": {"type": "object"}},
            "external_sources": {"type": "array", "items": {"type": "string", "format": "uri"}},
            "cta_strategy": {"type": "string"},
            "schema_strategy": {"type": "array", "items": {"type": "string"}},
            "ai_sourceability_requirements": {"type": "array", "items": {"type": "string"}},
            "brand_voice": {"type": "string"},
            "content_constraints": {"type": "array", "items": {"type": "string"}},
            "success_metrics": {"type": "object"},
            "approval_required": {"type": "string", "enum": ["LEVEL_A", "LEVEL_B", "LEVEL_C"]},
            "created_by": {"type": "string"},
            "created_at": {"type": "string", "format": "date-time"}
        },
        required=["brief_id", "page_id", "opportunity_id", "primary_keyword", "search_intent", "commercial_intent", "audience", "page_role", "recommended_title", "recommended_meta", "recommended_h1", "recommended_h2s", "cta_strategy", "brand_voice", "success_metrics", "approval_required", "created_by", "created_at"]
    ),

    "content_change": create_schema(
        "Content Change",
        "Atomic, traceable content mutation submitted for Sentinel approval and Mechanic execution.",
        {
            "change_id": {"type": "string"},
            "page_id": {"type": "string"},
            "content_version_before": {"type": "string"},
            "content_version_after": {"type": "string"},
            "change_type": {
                "type": "string",
                "enum": ["TITLE", "META", "H1", "H2", "H3", "BODY", "FAQ", "INTERNAL_LINK", "ALT_TEXT", "SCHEMA", "CTA", "STRUCTURE", "FULL_REWRITE", "OTHER"]
            },
            "old_value": {"type": "string"},
            "new_value": {"type": "string"},
            "reason": {"type": "string"},
            "keyword_id": {"type": ["string", "null"]},
            "evidence": {"type": "string"},
            "hypothesis": {"type": "string"},
            "expected_impact": {"type": "string", "enum": ["HIGH", "MEDIUM", "LOW"]},
            "agent": {"type": "string"},
            "reviewer": {"type": ["string", "null"]},
            "approval_status": {
                "type": "string",
                "enum": ["PENDING", "APPROVED", "REJECTED", "CHANGES_REQUESTED"]
            },
            "implementation_status": {
                "type": "string",
                "enum": ["PLANNED", "IN_PROGRESS", "IMPLEMENTED", "ROLLED_BACK"]
            },
            "implemented_at": {"type": ["string", "null"], "format": "date-time"},
            "verification_status": {
                "type": "string",
                "enum": ["VERIFIED", "FAILED", "PENDING"]
            },
            "verification_date": {"type": ["string", "null"], "format": "date-time"}
        },
        required=["change_id", "page_id", "content_version_before", "content_version_after", "change_type", "old_value", "new_value", "reason", "evidence", "hypothesis", "expected_impact", "agent", "approval_status", "implementation_status", "verification_status"]
    ),

    "content_version": create_schema(
        "Content Version",
        "Reversible point-in-time snapshot of page markup, content, and metadata.",
        {
            "version_id": {"type": "string"},
            "page_id": {"type": "string"},
            "version_number": {"type": "integer", "minimum": 1},
            "content_snapshot": {"type": "string"},
            "title": {"type": "string"},
            "meta_description": {"type": "string"},
            "h1": {"type": "string"},
            "h2s": {"type": "array", "items": {"type": "string"}},
            "h3s": {"type": "array", "items": {"type": "string"}},
            "schema_snapshot": {"type": ["object", "null"]},
            "internal_links": {"type": "array", "items": {"type": "object"}},
            "created_at": {"type": "string", "format": "date-time"},
            "created_by": {"type": "string"},
            "reason": {"type": "string"},
            "status": {"type": "string", "enum": ["ACTIVE", "ARCHIVED", "DRAFT"]}
        },
        required=["version_id", "page_id", "version_number", "content_snapshot", "title", "meta_description", "h1", "created_at", "created_by", "reason", "status"]
    ),

    "ai_visibility": create_schema(
        "AI Visibility Record",
        "Observation of brand/property presence in generative AI answers and summaries.",
        {
            "visibility_id": {"type": "string"},
            "query": {"type": "string"},
            "keyword_id": {"type": ["string", "null"]},
            "platform": {
                "type": "string",
                "enum": ["GOOGLE_AI_OVERVIEW", "GOOGLE_AI_MODE", "CHATGPT", "PERPLEXITY", "COPILOT", "GEMINI", "OTHER"]
            },
            "country": {"type": "string"},
            "location": {"type": "string"},
            "language": {"type": "string"},
            "device": {"type": "string"},
            "date": {"type": "string", "format": "date"},
            "mentioned": {"type": ["boolean", "null"], "description": "Strictly null if not directly measurable."},
            "cited": {"type": ["boolean", "null"], "description": "Strictly null if not directly measurable."},
            "citation_url": {"type": ["string", "null"], "format": "uri"},
            "citation_title": {"type": ["string", "null"]},
            "competitors_mentioned": {"type": "array", "items": {"type": "string"}},
            "competitor_citations": {"type": "array", "items": {"type": "string", "format": "uri"}},
            "answer_type": {"type": ["string", "null"]},
            "source_type": {"type": ["string", "null"]},
            "observation_method": {
                "type": "string",
                "enum": ["DIRECT", "API", "MANUAL", "THIRD_PARTY", "NOT_MEASURABLE"]
            },
            "confidence": {"type": "string", "enum": ["HIGH", "MEDIUM", "LOW", "UNKNOWN"]},
            "notes": {"type": ["string", "null"]}
        },
        required=["visibility_id", "query", "platform", "country", "location", "language", "device", "date", "observation_method", "confidence"]
    ),

    "forecast": create_schema(
        "Forecast",
        "P10/P50/P90 predictive range model for keyword ranking and inquiry trajectories.",
        {
            "forecast_id": {"type": "string"},
            "date_created": {"type": "string", "format": "date-time"},
            "keyword_id": {"type": "string"},
            "page_id": {"type": "string"},
            "baseline_position": {"type": "number"},
            "target_position": {"type": "number"},
            "forecast_window": {
                "type": "string",
                "enum": ["1_4_WEEKS", "4_8_WEEKS", "8_12_WEEKS", "3_6_MONTHS", "6_12_MONTHS", "UNKNOWN"]
            },
            "expected_result": {
                "type": "object",
                "properties": {
                    "p10_pessimistic": {"type": "number"},
                    "p50_realistic": {"type": "number"},
                    "p90_optimistic": {"type": "number"},
                    "expected_impressions": {"type": ["integer", "null"]},
                    "expected_ctr": {"type": ["number", "null"]},
                    "expected_inquiries": {"type": ["integer", "null"]}
                },
                "required": ["p10_pessimistic", "p50_realistic", "p90_optimistic"]
            },
            "confidence": {"type": "string", "enum": ["HIGH", "MEDIUM", "LOW", "UNKNOWN"]},
            "assumptions": {"type": "array", "items": {"type": "string"}},
            "dependencies": {"type": "array", "items": {"type": "string"}},
            "risks": {"type": "array", "items": {"type": "string"}},
            "recommended_actions": {"type": "array", "items": {"type": "string"}},
            "actual_result": {"type": ["object", "null"]},
            "actual_date": {"type": ["string", "null"], "format": "date-time"},
            "forecast_error": {"type": ["number", "null"], "description": "Calculated Prediction Error Score (PES)"},
            "calibration_status": {
                "type": "string",
                "enum": ["PENDING", "CALIBRATED", "MISCALIBRATED"]
            }
        },
        required=["forecast_id", "date_created", "keyword_id", "page_id", "baseline_position", "target_position", "forecast_window", "expected_result", "confidence", "calibration_status"]
    ),

    "experiment": create_schema(
        "Experiment",
        "Controlled on-page, architectural, or internal linking SEO test.",
        {
            "experiment_id": {"type": "string"},
            "name": {"type": "string"},
            "hypothesis": {"type": "string"},
            "page_ids": {"type": "array", "items": {"type": "string"}},
            "keyword_ids": {"type": "array", "items": {"type": "string"}},
            "baseline": {"type": "object"},
            "change": {"type": "string"},
            "start_date": {"type": "string", "format": "date"},
            "end_date": {"type": "string", "format": "date"},
            "expected_result": {"type": "string"},
            "success_metric": {"type": "string"},
            "control": {"type": ["object", "null"]},
            "variant": {"type": ["object", "null"]},
            "actual_result": {"type": ["object", "null"]},
            "statistical_confidence": {
                "type": "string",
                "enum": ["HIGH", "MEDIUM", "LOW", "INCONCLUSIVE"]
            },
            "conclusion": {"type": ["string", "null"]},
            "learning": {"type": ["string", "null"]},
            "next_action": {"type": ["string", "null"]},
            "status": {
                "type": "string",
                "enum": ["PLANNED", "RUNNING", "COMPLETED", "ABORTED", "INCONCLUSIVE"]
            },
            "owner": {"type": "string"}
        },
        required=["experiment_id", "name", "hypothesis", "page_ids", "keyword_ids", "baseline", "change", "start_date", "end_date", "expected_result", "success_metric", "statistical_confidence", "status", "owner"]
    ),

    "knowledge_fact": create_schema(
        "Knowledge Fact",
        "Granular verified ground-truth fact maintained by Archivist (#2).",
        {
            "fact_id": {"type": "string"},
            "subject": {"type": "string"},
            "predicate": {"type": "string"},
            "object": {"type": "string"},
            "entity_id": {"type": "string"},
            "value": {"type": "string"},
            "unit": {"type": ["string", "null"]},
            "source": {"type": "string"},
            "source_url": {"type": ["string", "null"], "format": "uri"},
            "verified": {"type": "boolean"},
            "verification_status": {
                "type": "string",
                "enum": ["VERIFIED", "PARTIALLY_VERIFIED", "UNVERIFIED", "CONFLICTING"]
            },
            "verified_by": {"type": "string"},
            "verified_at": {"type": "string", "format": "date-time"},
            "expires_at": {"type": ["string", "null"], "format": "date-time"},
            "notes": {"type": ["string", "null"]}
        },
        required=["fact_id", "subject", "predicate", "object", "entity_id", "value", "source", "verified", "verification_status", "verified_by", "verified_at"]
    ),

    "claim": create_schema(
        "Claim",
        "Brand, property, or amenity assertion requiring Sentinel verification before publication.",
        {
            "claim_id": {"type": "string"},
            "claim_text": {"type": "string"},
            "entity_id": {"type": "string"},
            "property_id": {"type": ["string", "null"]},
            "status": {
                "type": "string",
                "enum": ["VERIFIED", "REJECTED", "UNVERIFIED", "CONDITIONAL"]
            },
            "evidence": {"type": "string"},
            "verification_source": {"type": "string"},
            "verified_by": {"type": "string"},
            "verified_at": {"type": "string", "format": "date-time"}
        },
        required=["claim_id", "claim_text", "entity_id", "status", "evidence", "verification_source", "verified_by", "verified_at"]
    ),

    "learning": create_schema(
        "Learning",
        "Bayesian strategic inference derived from verified performance telemetry or experiments.",
        {
            "learning_id": {"type": "string"},
            "date": {"type": "string", "format": "date"},
            "category": {"type": "string"},
            "source_experiment_id": {"type": ["string", "null"]},
            "observation": {"type": "string"},
            "insight": {"type": "string"},
            "actionable_takeaway": {"type": "string"},
            "confidence": {"type": "string", "enum": ["HIGH", "MEDIUM", "LOW"]},
            "recorded_by": {"type": "string"}
        },
        required=["learning_id", "date", "category", "observation", "insight", "actionable_takeaway", "confidence", "recorded_by"]
    ),

    "strategic_rule": create_schema(
        "Strategic Rule",
        "Permanent operational heuristic or hard constraint governed by Sentinel and Archivist.",
        {
            "rule_id": {"type": "string"},
            "rule_title": {"type": "string"},
            "rule_statement": {"type": "string"},
            "category": {
                "type": "string",
                "enum": ["LUXURY_VOICE", "ENTITY_FACT", "TECHNICAL_SEO", "SCHEMA", "SAFETY_VETO", "DEPLOYMENT"]
            },
            "enforcement_level": {
                "type": "string",
                "enum": ["MANDATORY", "HIGH_RECOMMENDATION", "GUIDELINE"]
            },
            "active": {"type": "boolean"},
            "created_at": {"type": "string", "format": "date-time"}
        },
        required=["rule_id", "rule_title", "rule_statement", "category", "enforcement_level", "active", "created_at"]
    ),

    "strategy_state": create_schema(
        "Strategy State",
        "Real-time operational snapshot of the 21-agent autonomous growth system.",
        {
            "state_id": {"type": "string"},
            "date": {"type": "string", "format": "date"},
            "current_phase": {"type": "string"},
            "north_star": {
                "type": "object",
                "properties": {
                    "target_quarter": {"type": "string"},
                    "target_inquiries": {"type": "integer"},
                    "current_inquiries": {"type": "integer"},
                    "focus_markets": {"type": "array", "items": {"type": "string"}},
                    "focus_entities": {"type": "array", "items": {"type": "string"}}
                },
                "required": ["target_quarter", "focus_markets", "focus_entities"]
            },
            "top_priorities": {"type": "array", "items": {"type": "string"}},
            "top_opportunities": {"type": "array", "items": {"type": "string"}},
            "top_risks": {"type": "array", "items": {"type": "string"}},
            "active_experiments": {"type": "array", "items": {"type": "string"}},
            "recent_learnings": {"type": "array", "items": {"type": "string"}},
            "forecast_summary": {"type": ["object", "null"]},
            "competitor_summary": {"type": ["object", "null"]},
            "ai_visibility_summary": {"type": ["object", "null"]},
            "next_best_action": {"type": "object"},
            "reason": {"type": "string"},
            "updated_by": {"type": "string"}
        },
        required=["state_id", "date", "current_phase", "north_star", "top_priorities", "top_opportunities", "top_risks", "active_experiments", "recent_learnings", "next_best_action", "reason", "updated_by"]
    ),

    "next_best_action": create_schema(
        "Next Best Action",
        "Highest priority next action decided by Conductor (#1) for immediate execution.",
        {
            "action_id": {"type": "string"},
            "date": {"type": "string", "format": "date"},
            "action": {"type": "string"},
            "page_id": {"type": "string"},
            "keyword_id": {"type": ["string", "null"]},
            "opportunity_id": {"type": ["string", "null"]},
            "reason": {"type": "string"},
            "evidence": {"type": "string"},
            "expected_impact": {"type": "string", "enum": ["HIGH", "MEDIUM", "LOW"]},
            "effort": {"type": "string", "enum": ["LOW", "MEDIUM", "HIGH"]},
            "confidence": {"type": "string", "enum": ["HIGH", "MEDIUM", "LOW", "UNKNOWN"]},
            "dependencies": {"type": "array", "items": {"type": "string"}},
            "owner": {"type": "string"},
            "approval_required": {"type": "string", "enum": ["LEVEL_A", "LEVEL_B", "LEVEL_C"]},
            "deadline": {"type": "string", "format": "date-time"},
            "status": {
                "type": "string",
                "enum": ["PENDING", "APPROVED", "IN_PROGRESS", "COMPLETED", "ABORTED"]
            }
        },
        required=["action_id", "date", "action", "page_id", "reason", "evidence", "expected_impact", "effort", "confidence", "owner", "approval_required", "deadline", "status"]
    ),

    "kpi_baseline": create_schema(
        "KPI Baseline",
        "Historical ground-truth performance baseline across GSC, GA4, Bing, and Direct Inquiries.",
        {
            "baseline_id": {"type": "string"},
            "property_name": {"type": "string"},
            "period_start": {"type": "string", "format": "date"},
            "period_end": {"type": "string", "format": "date"},
            "gsc_clicks": {"type": "integer"},
            "gsc_impressions": {"type": "integer"},
            "gsc_avg_ctr": {"type": "number"},
            "gsc_avg_position": {"type": "number"},
            "ga4_total_users": {"type": "integer"},
            "ga4_sessions": {"type": "integer"},
            "ga4_engagement_rate": {"type": "number"},
            "direct_inquiries": {"type": "integer"},
            "created_at": {"type": "string", "format": "date-time"},
            "verified_by": {"type": "string"}
        },
        required=["baseline_id", "property_name", "period_start", "period_end", "gsc_clicks", "gsc_impressions", "gsc_avg_ctr", "gsc_avg_position", "ga4_total_users", "ga4_sessions", "created_at", "verified_by"]
    ),

    "structured_data": create_schema(
        "Structured Data Record",
        "JSON-LD Schema definition deployed to an entity or route.",
        {
            "schema_id": {"type": "string"},
            "page_id": {"type": "string"},
            "schema_type": {
                "type": "string",
                "enum": ["LodgingBusiness", "HotelRoom", "Resort", "FAQPage", "BreadcrumbList", "Article", "LocalBusiness", "ItemPage", "AboutPage", "ContactPage"]
            },
            "jsonld_content": {"type": "object"},
            "validation_status": {"type": "string", "enum": ["VALID", "SYNTAX_ERROR", "MISSING_RECOMMENDED_FIELD", "UNVERIFIED"]},
            "google_rich_result_eligible": {"type": "boolean"},
            "last_audited_at": {"type": "string", "format": "date-time"}
        },
        required=["schema_id", "page_id", "schema_type", "jsonld_content", "validation_status", "google_rich_result_eligible", "last_audited_at"]
    )
}

def main():
    os.makedirs(SCHEMA_DIR, exist_ok=True)
    count = 0
    for name, schema_obj in SCHEMAS.items():
        filename = f"{name}.json"
        filepath = os.path.join(SCHEMA_DIR, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(schema_obj, f, indent=2)
        print(f"Generated: {filepath}")
        count += 1
    print(f"\nSuccessfully generated {count} machine-readable JSON schemas in {SCHEMA_DIR}")

if __name__ == "__main__":
    main()
