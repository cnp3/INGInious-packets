#!/usr/bin/env python3
import os, os.path, shutil

course_name = 'CNP3'

os.mkdir(course_name)

dir = os.scandir('.')

for item in dir:
    if item.name != course_name and (item.is_dir() or item.name == 'course.yaml'):
        try:
            os.mkdir(os.path.join(item.name, 'test'))
        except:
            pass  # test directory already existing
        shutil.move('./' + item.name, os.path.join(course_name, item.name))
