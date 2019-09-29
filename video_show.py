#!/usr/bin/python3
import cv2
import argparse
import os

def get_args():
    parser = argparse.ArgumentParser(description='Capture video.')
    parser.add_argument('--camera_index', type=int, default=0, help='Camera index.')
    parser.add_argument('--width', type=int, help='Video width.')
    parser.add_argument('--height', type=int, help='Video height.')
    return parser.parse_args()

if __name__ == '__main__':

    args = get_args()

    cap = cv2.VideoCapture(args.camera_index)
    
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) if args.width == None else args.width
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) if args.height == None else args.height
    fourcc = cv2.VideoWriter_fourcc(*'XVID')   

    while True:
        ret, frame = cap.read()
        cv2.imshow('Results', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
