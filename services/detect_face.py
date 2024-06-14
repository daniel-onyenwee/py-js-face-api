import json
from utils import base64_to_image, is_valid_base64
from utils.face_recognition import face_locations

def detect_face(models, face_base64_string:str, pretty_print:bool = False) -> str:
    json_indent = None

    if pretty_print == True:
        json_indent = 2

    if face_base64_string == "":
        return json.dumps({
            "ok": False,
            "error": {
                "message": "Missing parameter 'face_image_data'",
                "code": 1001
            },
            "data": None
        }, indent=json_indent)

    if not is_valid_base64(face_base64_string):
        return json.dumps({
            "ok": False,
            "error": {
                "message": "Invalid face_image_data format",
                "code": 1002
            },
            "data": None
        }, indent=json_indent)
    
    try:
        image = base64_to_image(face_base64_string)
    except Exception as e:
        return json.dumps({
            "ok": False,
            "error": {
                "message": "Invalid face_image_data format",
                "code": 1002
            },
            "data": None
        }, indent=json_indent)
    
    faces = face_locations(models, image)

    return json.dumps({
        "ok": True,
        "error": None,
        "data": {
            "face_count": len(faces)
        }
    }, indent=json_indent)