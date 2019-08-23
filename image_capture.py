import cv2
import argparse
import os

parser = argparse.ArgumentParser(description='Capture image')
parser.add_argument('--camera_index', type=int, default=0, help='Camera index.')
parser.add_argument('--save_dir', type=str, default='./data/images/', help='Save dir')
parser.add_argument('--width', type=int, help='Video width.')
parser.add_argument('--height', type=int, help='Video height.')
args = parser.parse_args()

if __name__ == '__main__':
    assert(len(args.save_dir) > 0)

    cap = cv2.VideoCapture(args.camera_index)

    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) if args.width == None else args.width
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) if args.height == None else args.height
    
    if not os.path.exists(args.save_dir):
        os.mkdir(args.save_dir)

    idx = 0
    while True:
        ret, frame = cap.read()
        cv2.imshow('Capture', frame)

        if cv2.waitKey(1) & 0xFF == ord('s'):   
            file_name = args.save_dir + str(idx) + '.png'
            cv2.imwrite(file_name, frame) 
            print('Saved image to ', file_name)
            idx += 1  
            
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
