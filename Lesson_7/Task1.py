import os

my_project = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}


def make_dir(my_file):
    for f, f_s in my_file.items():
        if not os.path.exists(f):
            for i in range(len(f_s)):
                os.makedirs(os.path.join(f, f_s[i]))


make_dir(my_project)
