import json
import logging

def validate_and_parse_tool_payload(raw_payload: str) -> dict:
    """Safely parses and validates tool-calling JSON payloads, handling malformed data gracefully."""
    if not raw_payload or not isinstance(raw_payload, str):
        raise ValueError("Payload must be a non-empty string")
    
    try:
        parsed = json.loads(raw_payload)
    except json.JSONDecodeError as e:
        logging.error(f"Malformed JSON payload encountered: {e}")
        return {"error": "Invalid JSON format", "details": str(e), "status": "rejected"}
        
    if not isinstance(parsed, dict) or "tool" not in parsed:
        return {"error": "Missing required 'tool' field in schema", "status": "rejected"}
        
    return {"status": "success", "data": parsed}
