import os
import dlib

def load_models(models_dir:str):
    pose_predictor_68_point = dlib.shape_predictor(pose_predictor_model_location(models_dir))
    face_encoder = dlib.face_recognition_model_v1(face_recognition_model_location(models_dir))
    cnn_face_detector = dlib.cnn_face_detection_model_v1(cnn_face_detector_model_location(models_dir))
    pose_predictor_5_point = dlib.shape_predictor(pose_predictor_five_point_model_location(models_dir))

    return ({
        "pose_predictor_68_point": pose_predictor_68_point,
        "face_encoder": face_encoder,
        "cnn_face_detector": cnn_face_detector,
        "pose_predictor_5_point": pose_predictor_5_point
    })

def pose_predictor_model_location(models_dir:str):    
    return os.path.join(models_dir, "shape_predictor_68_face_landmarks.dat")

def pose_predictor_five_point_model_location(models_dir:str):    
    return os.path.join(models_dir, "shape_predictor_5_face_landmarks.dat")

def face_recognition_model_location(models_dir:str):
    return os.path.join(models_dir, "dlib_face_recognition_resnet_model_v1.dat")

def cnn_face_detector_model_location(models_dir:str):    
    return os.path.join(models_dir, "mmod_human_face_detector.dat")