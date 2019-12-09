import os
import sys
import shutil
import argparse

def get_args():
    parser = argparse.ArgumentParser(description='Image processing utilities.')
    parser.add_argument('--mode', type=int, default=0, help='Processing mode.')
    parser.add_argument('--source_dir', type=str, help='Source directory of images.')
    parser.add_argument('--dest_dir', type=str, help='Destination directory of images.')
    parser.add_argument('--save_path', type=str, help='Save path of output images.')
    
    return parser.parse_args()


def get_files_path(dir, save_path):
    for root, _, files in os.walk(dir):
        for f in files:
            path = os.path.abspath(os.path.join(root, f))
            print(path)
            if os.path.isfile(save_path):
                with open(save_path, 'a') as f:
                    f.write(path + '\n')
            else:
                with open(save_path, 'w') as f:
                    f.write(path + '\n')


def copy_files(source_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)

    for root, _, files in os.walk(source_dir):
        for f in files:
            source_path = os.path.abspath(os.path.join(root, f))
            dest_path = os.path.abspath(os.path.join(dest_dir, f))
            try:
                shutil.copy(source_path, dest_path)
                print('Copied {} to {}'.format(source_path, dest_path))
            except IOError as e:
                print('Unable to copy file. %s' % e)
            except:
                print('Unexpected error:', sys.exc_info())


if __name__ == '__main__':
    args = get_args()
    if args.mode == 0:
        get_files_path(args.source_dir, args.save_path)
    elif args.mode == 1:
        copy_files(args.source_dir, args.dest_dir)
    #get_files_path('./data/output', 'safety_work_images.txt')
    #source_dir = '/mnt/data/src/labelImg/data/downloads/Taisei_output'
    #dest_dir = '/mnt/data/src/labelImg/data/downloads/Taisei_demo/JPEGImages'
    #copy_file(source_dir, dest_dir)