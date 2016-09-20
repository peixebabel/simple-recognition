# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 09:31:54 2016

@author: Camila Laranjeira
"""

import numpy
import caffe
import matplotlib.pyplot as plt
from os import mkdir, listdir
from os.path import isdir, join, abspath
from constants import *

####### Initializing Net and Transformation object #######
caffe_root = '/home/laranjeira/caffe/'
# Download these files from
# https://gist.github.com/ksimonyan/3785162f95cd2d5fee77
model = "VGG_ILSVRC_19_layers_deploy.prototxt"
weights = "VGG_ILSVRC_19_layers.caffemodel"
# Which layer will provide your features? (see model file)
VGG_LAYER = "fc7"

caffe.set_mode_cpu()
net = caffe.Net(model, weights, caffe.TEST)
mean = numpy.load(
    caffe_root + 'python/caffe/imagenet/ilsvrc_2012_mean.npy').mean(1).mean(1)

transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
transformer.set_transpose('data', (2, 0, 1))
transformer.set_mean('data', mean)
transformer.set_raw_scale('data', 255)
transformer.set_channel_swap('data', (2, 1, 0))
# batch size, # 3-channel (BGR) images, # image size is 224x224
net.blobs['data'].reshape(1, 3, 224, 224)
###########################################################


def extractFeatures(path):
    image = caffe.io.load_image(path)
    transformed_image = transformer.preprocess('data', image)

    net.blobs['data'].data[...] = transformed_image
    net.forward()
    features = net.blobs[VGG_LAYER].data.copy()

    return features


def createLabelsFile(dataset_size, class_name, label):
    if not(isdir(labels_dir)):
        mkdir(labels_dir)
    filename = labels_dir + "labels_" + class_name + ".txt"
    labels_output = open(filename, 'w')
    for i in xrange(dataset_size):
        labels_output.write(str(label) + '\n')
    labels_output.close()


def storeFeatures(features, class_name):
    if not(isdir(features_dir)):
        mkdir(features_dir)
    filename = features_dir + "features_" + class_name + ".txt"
    features_output = open(filename, 'a')
    # 4096 is the size of the layer's output
    for i in xrange(4096):
        features_output.write(str(features[0][i]) + ' ')
    features_output.write('\n')
    features_output.close()


def saveNewClass(class_name, label):
    filename = dataset_root + "classes.txt"
    classes_output = open(filename, 'a')
    classes_output.write(class_name + ' ' + str(label) + '\n')
    classes_output.close()

if __name__ == "__main__":
    for k, class_dir in enumerate(listdir(join(dataset_root, images_dir))):
        saveNewClass(str(class_dir), k)
        image_files = sorted(listdir(
            join(dataset_root, images_dir, class_dir)))
        createLabelsFile(len(image_files), str(class_dir), k)
        print(str(class_dir))  # Status feedback on screen
        for image in image_files:
            features = extractFeatures(
                str(abspath(join(dataset_root, images_dir, class_dir, image))))
            storeFeatures(features, str(class_dir))
