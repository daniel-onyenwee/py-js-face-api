import base64

def is_valid_base64(base64_string: str) -> bool:
    try:
        base64.b64decode(base64_string, validate=True)
        return True
    except (base64.binascii.Error, ValueError):
        return False