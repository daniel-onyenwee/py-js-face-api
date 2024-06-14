import json
import os
from cli import py_js_face_api_cli
from services import detect_face, recognize_face
from utils.face_recognition import load_models

def main():
    args = py_js_face_api_cli.parse_args()

    json_indent = None

    if args.command == "detect":
        if args.pretty == True:
            json_indent = 2

        if not os.path.exists(args.models_dir):
            print(json.dumps({
                "ok": False,
                "error": {
                    "message": "Models directory not found",
                    "code": 1000
                },
                "data": None
            }, indent=json_indent))
            return
        
        models = load_models(args.models_dir)
        
        try:
            face_image_data = input("face_image_data: ")
        except:
            face_image_data = ""
            
        print(detect_face(models, face_image_data, pretty_print=args.pretty))
    elif args.command == "recognize":
        if args.pretty == True:
            json_indent = 2

        if not os.path.exists(args.models_dir):
            print(json.dumps({
                "ok": False,
                "error": {
                    "message": "Models directory not found",
                    "code": 1000
                },
                "data": None
            }, indent=json_indent))
            return
        
        models = load_models(args.models_dir)

        try:
            face_image_data = input("face_image_data: ")
        except:
            face_image_data = ""

        try:
            known_face_image_data = input("know_face_image_data: ")
        except:
            known_face_image_data = ""

        print(recognize_face(models, face_image_data, known_face_image_data, pretty_print=args.pretty))
    else:
        py_js_face_api_cli.print_help()

if __name__ == "__main__":
    main()