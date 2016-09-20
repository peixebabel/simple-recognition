# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 00:30:35 2016

@author: Camila Laranjeira
"""
import numpy as np
from sklearn import svm
from sklearn.cross_validation import KFold
from sklearn import preprocessing
from pickle import dump
from os import listdir
from os.path import join, abspath
from constants import *


def cross_validate(data, labels, classifier):
    """ data: [n_samples, n_features]
        labels: [n_samples] (value is 0 to n_labels)"""
    kf = KFold(labels.size, n_folds=10)
    scores = []
    for k, (train, test) in enumerate(kf):
        classifier = classifier.fit(data[train], labels[train])
        score = classifier.score(data[test], labels[test])
        scores.append(score)
        print('{} fold: {:.4f}'.format(k, score))

    return np.mean(scores)


def store_classifier(classifier):
     # ===== Store classifier ===== #
    dump(classifier, open('classifier.p', 'wb'))

if __name__ == '__main__':
    features_files = sorted(listdir(join(project_root, features_dir)))

    data = np.loadtxt(
        abspath(join(project_root, features_dir, features_files.pop())))
    for ffile in features_files:
        data = np.append(data, np.loadtxt(
            abspath(join(project_root, features_dir, ffile))), axis=0)

    labels_files = sorted(listdir(join(dataset_root, labels_dir)))

    labels = np.loadtxt(
        abspath(
            join(dataset_root, labels_dir, labels_files.pop())))

    for lfile in labels_files:
        labels = np.append(labels, np.loadtxt(
            abspath(join(dataset_root, labels_dir, lfile))), axis=0)

    data = preprocessing.scale(data)

    clf = svm.LinearSVC(class_weight='balanced', C=1e-4)
    acc = cross_validate(data, labels, clf)
    print('Mean accuracy: {:.4f}'.format(acc))

    clf = clf.fit(data, labels)
    store_classifier(clf)
