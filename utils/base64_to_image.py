import base64
from io import BytesIO
import numpy as np
from PIL import Image

def base64_to_image(base64_string:str):
    decoded_data  = base64.b64decode(base64_string)
    image_data = BytesIO(decoded_data)
    image = Image.open(image_data)
    return np.array(image)
