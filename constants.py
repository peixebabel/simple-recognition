# -*- coding: utf-8 -*-

from os.path import abspath

# '/home/laranjeira/projects/peixe-babel/simple-recognition/'
project_root = "{}/".format(abspath('.'))
features_dir = '{}features/'.format(project_root)

dataset_root = '{}dataset/'.format(project_root)
images_dir = '{}images/'.format(dataset_root)
labels_dir = '{}labels/'.format(dataset_root)
