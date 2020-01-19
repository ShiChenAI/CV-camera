import os
import sys
import shutil
import argparse
from PIL import Image

def get_args():
    parser = argparse.ArgumentParser(description='Image processing utilities.')
    parser.add_argument('--mode', type=int, default=0, help='Processing mode.')
    parser.add_argument('--source_dir', type=str, help='Source directory of images.')
    parser.add_argument('--dest_dir', type=str, help='Destination directory of images.')
    parser.add_argument('--save_path', type=str, help='Save path of output images.')
    
    return parser.parse_args()


def get_files_path(dir, save_path=''):
    files_list = []
    for root, _, files in os.walk(dir):
        for f in files:
            path = os.path.abspath(os.path.join(root, f))
            print(path)
            if os.path.isfile(save_path):
                if save_path != '':
                    with open(save_path, 'a') as f:
                        f.write(path + '\n')

                files_list.append(path)
            else:
                if save_path != '':
                    with open(save_path, 'w') as f:
                        f.write(path + '\n')

                files_list.append(path)
    
    return files_list

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

def convert_images(img_dir, output_dir, img_size=(480,360), target_type='png'):   
    img_list = os.listdir(img_dir)
    ori_files = [os.path.join(img_dir, _) for _ in img_list]
    for idx, ori_file in enumerate(ori_files):
        if idx > 10000:
            break
        try:
            sys.stdout.write('\rConverting image %d/10000 ' % (idx))
            sys.stdout.flush()
            img = Image.open(ori_file)
            img.thumbnail((img_size))
            output_path = os.path.split(ori_file)[0] + '.' + target_type
            img.save(output_path)
            shutil.move(output_path, output_dir)
        except IOError as e:
            print('Could not read: ', ori_file)
            print('Error: ', e)
            print('Skip it\n')
            

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