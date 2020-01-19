#!/usr/bin/python3
import cv2
import argparse
import os
import imageio
from utils import convert_images

def get_args():
    parser = argparse.ArgumentParser(description='Capture video.')
    parser.add_argument('--img_dir', type=str, default='', help='Images path.')
    parser.add_argument('--save_path', type=str, default='./data/output.gif', help='Save path.')
    parser.add_argument('--width', type=int, default=480, help='Images width.')
    parser.add_argument('--height', type=int, default=360, help='Images height.')
    parser.add_argument('--duration', type=float, default=0.1, help='Frame duration.')
    
    return parser.parse_args()


def create_gif(output_name, img_path, duration=0.1):
    frames = []
    png_files = os.listdir(img_path)
    img_list = [os.path.join(img_path, _) for _ in png_files]
    for img_file in img_list:
        frames.append(imageio.imread(img_file))

    imageio.mimsave(output_name, frames, 'GIF', duration=duration)


if __name__ == '__main__':

    args = get_args()
    assert(args.img_dir is not None)
    assert(args.save_path is not None)
    assert(args.width > 0)
    assert(args.height > 0)
    assert(args.duration > 0)

    png_dir = os.path.join(args.img_dir, 'temp')
    if not os.path.exists(png_dir):
        os.mkdir(png_dir)
    
    convert_images(args.img_dir, png_dir, img_size=(args.width, args.height))
    create_gif(args.save_path, png_dir, duration=args.duration)