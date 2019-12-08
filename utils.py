import os
import sys
import shutil

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


def copy_file(source_dir, dest_dir):
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
    #get_files_path('./data/output', 'safety_work_images.txt')
    source_dir = '/mnt/data/src/labelImg/data/downloads/Taisei_output'
    dest_dir = '/mnt/data/src/labelImg/data/downloads/Taisei_demo/JPEGImages'
    copy_file(source_dir, dest_dir)