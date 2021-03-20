from shutil import copytree
import os


def copy_fails():
    dir_base = 'FloderN1'
    name = 'Rock'
    for root, dirs, files in os.walk(dir_base):
        if root.find(name) > 0 and len(files) == 0:
            copytree(os.path.join(root), name, dirs_exist_ok=True)


if __name__ == '__main__':
    copy_fails()
