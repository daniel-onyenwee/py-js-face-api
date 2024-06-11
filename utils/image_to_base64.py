import base64

def image_to_base64(image_path:str):
    try:
        with open(image_path, "rb") as image_file:
            base64_string = base64.b64encode(image_file.read()).decode('utf-8')
            return base64_string
    except FileNotFoundError:
        print(f"Error: The file {image_path} was not found.")
        return None
    except Exception as e:
        print(f"Error: {str(e)}")
        return None