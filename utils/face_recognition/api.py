"""
Inspired by Adam Geitgey (ageitgey@gmail.com) face_recognition package
"""

import dlib
import numpy as np
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

face_detector = dlib.get_frontal_face_detector()

def _css_to_rect(css):
    return dlib.rectangle(css[3], css[0], css[1], css[2])

def _raw_face_landmarks(models, face_image, face_locations=None, model="large"):
    if face_locations is None:
        face_locations = _raw_face_locations(models, face_image)
    else:
        face_locations = [_css_to_rect(face_location) for face_location in face_locations]

    pose_predictor = models.get("pose_predictor_68_point")

    if model == "small":
        pose_predictor = models.get("pose_predictor_68_point")

    return [pose_predictor(face_image, face_location) for face_location in face_locations]

def face_encodings(models, face_image, known_face_locations=None, num_jitters=1, model="small"):
    face_encoder = models.get("face_encoder")
    raw_landmarks = _raw_face_landmarks(models, face_image, known_face_locations, model)
    return [np.array(face_encoder.compute_face_descriptor(face_image, raw_landmark_set, num_jitters)) for raw_landmark_set in raw_landmarks]

def _trim_css_to_bounds(css, image_shape):
    return max(css[0], 0), min(css[1], image_shape[1]), min(css[2], image_shape[0]), max(css[3], 0)

def _rect_to_css(rect):
    return rect.top(), rect.right(), rect.bottom(), rect.left()

def _raw_face_locations(models, img, number_of_times_to_upsample=1, model="hog"):
    if model == "cnn":
        return models.cnn_face_detector(img, number_of_times_to_upsample)
    else:
        return face_detector(img, number_of_times_to_upsample)

def face_locations(models, img, number_of_times_to_upsample=1, model="hog"):
    if model == "cnn":
        return [_trim_css_to_bounds(_rect_to_css(face.rect), img.shape) for face in _raw_face_locations(models, img, number_of_times_to_upsample, "cnn")]
    else:
        return [_trim_css_to_bounds(_rect_to_css(face), img.shape) for face in _raw_face_locations(models, img, number_of_times_to_upsample, model)]
    
def compare_faces(known_face_encodings, face_encoding_to_check, tolerance=0.6):
    return list(face_distance(known_face_encodings, face_encoding_to_check) <= tolerance)

def face_distance(face_encodings, face_to_compare):
    if len(face_encodings) == 0:
        return np.empty((0))

    return np.linalg.norm(face_encodings - face_to_compare, axis=1)