import json
import face_recognition
from utils import base64_to_image, is_valid_base64

def recognize_face(face_base64_string:str, know_face_base64_string:str, pretty_print:bool = False) -> str:
    json_indent = None

    if pretty_print == True:
        json_indent = 2

    if face_base64_string == "":
        return json.dumps({
            "ok": False,
            "error": {
                "message": "Message parameter 'face_image_data'",
                "code": 1000
            },
            "data": None
        }, indent=json_indent)

    if not is_valid_base64(face_base64_string):
        return json.dumps({
            "ok": False,
            "error": {
                "message": "Invalid face_image_data format",
                "code": 1001
            },
            "data": None
        }, indent=json_indent)
    
    try:
        face_image = base64_to_image(face_base64_string)
    except Exception as e:
        return json.dumps({
            "ok": False,
            "error": {
                "message": "Invalid face_image_data format",
                "code": 1001
            },
            "data": None
        }, indent=json_indent)
    
    if know_face_base64_string == "":
        return json.dumps({
            "ok": False,
            "error": {
                "message": "Message parameter 'know_face_image_data'",
                "code": 1002
            },
            "data": None
        }, indent=json_indent)
    
    if not is_valid_base64(know_face_base64_string):
        return json.dumps({
            "ok": False,
            "error": {
                "message": "Invalid know_face_image_data format",
                "code": 1003
            },
            "data": None
        }, indent=json_indent)
    
    try:
        know_face_image = base64_to_image(know_face_base64_string)
    except Exception as e:
        return json.dumps({
            "ok": False,
            "error": {
                "message": "Invalid know_face_image_data format",
                "code": 1003
            },
            "data": None
        }, indent=json_indent)
    

    face_image_encoding = face_recognition.face_encodings(face_image)

    if not face_image_encoding:
        return json.dumps({
            "ok": False,
            "error": {
                "message": "No face_image found",
                "code": 1004
            },
            "data": None
        }, indent=json_indent)
    
    if len(face_image_encoding) >= 2:
        return json.dumps({
            "ok": False,
            "error": {
                "message": "More than one face_image found",
                "code": 1004
            },
            "data": None
        }, indent=json_indent)
    
    know_face_image_encoding = face_recognition.face_encodings(know_face_image)

    if not know_face_image_encoding:
        return json.dumps({
            "ok": False,
            "error": {
                "message": "No know_face_image found",
                "code": 1005
            },
            "data": None
        }, indent=json_indent)
    
    if len(know_face_image_encoding) >= 2:
        return json.dumps({
            "ok": False,
            "error": {
                "message": "More than one know_face_image found",
                "code": 1006
            },
            "data": None
        }, indent=json_indent)
    
    match_results = face_recognition.compare_faces([know_face_image_encoding[0]], face_image_encoding[0])
    
    if match_results[0]:
        return json.dumps({
            "ok": True,
            "error":None,
            "data": None
        }, indent=json_indent)
    else:
        return json.dumps({
            "ok": False,
            "error": {
                "message": "Faces do not match",
                "code": 1007
            },
            "data": None
        }, indent=json_indent)
