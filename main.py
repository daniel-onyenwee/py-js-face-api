from cli import PyJsFaceApiCli
from services import detect_face, recognize_face

def main():
    args = PyJsFaceApiCli.parse_args()

    if args.command == "detect":
        try:
            face_image_data = input("face_image_data: ")
        except:
            face_image_data = ""
            
        print(detect_face(face_image_data, args.pretty))
    elif args.command == "recognize":
        try:
            face_image_data = input("face_image_data: ")
        except:
            face_image_data = ""

        try:
            known_face_image_data = input("know_face_image_data: ")
        except:
            known_face_image_data = ""

        print(recognize_face(face_image_data, known_face_image_data, args.pretty))
    else:
        PyJsFaceApiCli.print_help()

if __name__ == "__main__":
    main()