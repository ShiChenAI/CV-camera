import os

def get_files_path(dir, save_path):
    for root, dirs, files in os.walk(dir):
        for file in files:
            path = os.path.abspath(os.path.join(root, file))
            print(path)
            if os.path.isfile(save_path):
                with open(save_path, 'a') as f:
                    f.write(path + '\n')
            else:
                with open(save_path, 'w') as f:
                    f.write(path + '\n')

if __name__ == '__main__':
    get_files_path('./data/output', 'safety_work_images.txt')