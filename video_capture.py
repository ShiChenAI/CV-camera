#!/usr/bin/python3
import cv2
import argparse
import os

parser = argparse.ArgumentParser(description='Capture video')
parser.add_argument('--camera_index', type=int, default=0, help='Camera index.')
parser.add_argument('--save_path', type=str, default='./data/output.avi', help='Save path.')
parser.add_argument('--width', type=int, help='Video width.')
parser.add_argument('--height', type=int, help='Video height.')
parser.add_argument('--fps', type=int, default=30, help='Recording fps.')
args = parser.parse_args()

if __name__ == '__main__':

    assert(len(args.save_path) > 0)
    assert(args.save_path.fps > 0)
    
    cap = cv2.VideoCapture(args.camera_index)
    
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) if args.width == None else args.width
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) if args.height == None else args.height
    fourcc = cv2.VideoWriter_fourcc(*'XVID')   

    file_dir = os.path.dirname(args.save_path)
    if len(file_dir) > 0 and not os.path.exists(file_dir):
        os.mkdir(file_dir)

    out = cv2.VideoWriter()
    out.open(args.save_path, fourcc, args.fps, (w, h), True)

    while True:
        ret, frame=cap.read()
        cv2.imshow('Results', frame)
        out.write(frame)
        if cv2.waitKey(1) & 0xFF==ord('q') or ret==False:
            break

    cap.release()
    out.release()
