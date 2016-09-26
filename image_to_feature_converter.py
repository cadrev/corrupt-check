# coding: utf-8

import numpy as np
import os
import cv2
import pandas as pd
import matplotlib.cm as cm
from matplotlib import pyplot as plt



# Directory of the samples for converting to files

samples  = 'bad'
filename = samples + '_samples.csv'
features = []
labels   = []


data_dir = os.listdir(samples)

# Converting every image to a magnitude spectrum, using it as a feature for 
# machine learning makes the classification problem easier.

for i in data_dir:
    img    = cv2.imread(samples+'/'+i)
    f      = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    magnitude_spectrum = 20*np.log(np.abs(fshift))
    compressed         = cv2.resize(magnitude_spectrum,(32,32))
    flattened  = compressed.flatten()
    features.append(flattened)
    labels.append(0)    


# Convert the array into a dataframe
data            = pd.DataFrame(features)
data['labels']  = labels
data.head(1)

# remove NA values
data = data.fillna(0)

# save as csv
data.to_csv(filename,sep=',', index=False)






