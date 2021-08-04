#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

#  Author: David Arroyo Menéndez <davidam@gmail.com>
#  Maintainer: David Arroyo Menéndez <davidam@gmail.com>

# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.


import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
import argparse
import sys
from app.dame_utils import DameUtils

parser = argparse.ArgumentParser()
parser.add_argument('--csv')
show_parser = parser.add_mutually_exclusive_group(required=False)
show_parser.add_argument('--show', dest='show', action='store_true')
show_parser.add_argument('--no-show', dest='show', action='store_false')
parser.set_defaults(show=True)
args = parser.parse_args()

du = DameUtils()

if (len(sys.argv) > 1):
    data = np.genfromtxt(args.csv, delimiter=',', dtype='float64')
    scaler = MinMaxScaler(feature_range=[0, 1])
    data_rescaled = scaler.fit_transform(data[1:, 0:8])

    # Fitting the PCA algorithm with our Data
    pca = PCA().fit(data_rescaled)
    # Plotting the Cumulative Summation of the Explained Variance
    plt.figure()
    plt.plot(np.cumsum(pca.explained_variance_ratio_))
    plt.xlabel('Number of Components')
    plt.ylabel('Variance (%)')  # for each component
    plt.title('Dataset Explained Variance')
    string1 = 'files/images/pca_components_'
    string1 = string1 + str(du.path2file(args.csv)) + '.png'
    plt.savefig(string1)
    if (args.show):
        plt.show()
else:
    print("You must introduce a csv file.")
    print("Try $ python3 pca-components.py --csv='files/features_list.csv'")
