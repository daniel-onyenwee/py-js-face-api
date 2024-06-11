import argparse

parser = argparse.ArgumentParser(prog="PyJsFaceApi", description="A CLI tool for face detection and recognition.")

subparsers = parser.add_subparsers(dest="command", help="Sub-commands: 'detect' and 'recognize'")

 # Sub-parser for face detection
parser_detect  = subparsers.add_parser("detect", help="Detect faces in an image.")
parser_detect.add_argument("-p", "--pretty", action="store_false", help="Pretty print the CLI result.")

# Sub-parser for face recognition
parser_recognize = subparsers.add_parser("recognize", help="Recognize faces in an image based on known faces.")
parser_recognize.add_argument("-p", "--pretty", action="store_false", help="Pretty print the CLI result.")