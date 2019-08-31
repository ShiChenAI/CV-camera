#!/usr/bin/python3
import cv2
import argparse
import os

def get_args():
    parser = argparse.ArgumentParser(description='Video to images.')
    parser.add_argument('--video_dir', type=str, help='Save path of videos.')
    parser.add_argument('--video_name', type=str, help='Video name.')
    parser.add_argument('--batch_process', type=int, default=0, help='Batch process videos.')
    parser.add_argument('--save_path', type=str, help='Save path of output images.')
    
    return parser.parse_args()

def process_video(file_name, save_path):
    cap = cv2.VideoCapture(file_name)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    fps = cap.get(cv2.CAP_PROP_FPS)
    size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

    if not os.path.exists(save_path):
        os.mkdir(save_path)

    i = 1
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            output_name = os.path.splitext(os.path.split(file_name)[1])[0] + '_{}.jpg'.format(i)
            output_path = os.path.join(save_path, output_name)
            cv2.imwrite(output_path, frame)
            print('Saved frame {}'.format(output_path))
            i += 1
        else:
            break

    cap.release()


def batch_process(video_dir, save_dir, split_save=True):
    for root, dirs, files in os.walk(video_dir):
        if split_save:
            save_path = os.path.join(save_dir, dirs)
            if not os.path.exists(save_path):
                os.mkdir(save_path)
        for file in files:
            if split_save:
                save_path = os.path.join(save_dir, os.path.splitext(file)[0])
                if not os.path.exists(save_path):
                    os.mkdir(save_path)

            file_name = os.path.join(root, file)
            process_video(file_name, save_path)


if __name__ == '__main__':
    
    args = get_args()
    assert(len(args.save_path) > 0)

    if args.batch_process == 1:
        assert(len(args.video_dir) > 0)
        if not os.path.exists(args.save_path):
            os.mkdir(args.save_path)
        batch_process(args.video_dir, args.save_path)
    elif args.batch_process == 0:
        assert(len(args.video_name) > 0)
        process_video(args.video_name, args.save_path)
