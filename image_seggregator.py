# coding: utf-8



import numpy  as np
import pandas as pd
import cv2
from   sklearn.ensemble import ExtraTreesClassifier

import matplotlib.cm as cm
from matplotlib import pyplot as plt




# The training set is a processed data set of previous images
# containing good and bad samples from various UrbanFlood Stations. 

training = pd.read_csv('training_set.csv', sep=',')
labels   = training['labels']
features = training.values
del training['labels']


# Use a simple ExtraTrees Classifier.
et = ExtraTreesClassifier(n_estimators=1000)
et.fit(features, labels)


# Open the testing file to determine the accuracy of the
# classifier
test_data = pd.read_csv('good_samples.csv',sep=',')
test_labels          = test_data['labels']
test_features        = test_data.values
test_data['predict'] = et.predict(test_features)

# Change the > 0 to < 1 if the bad examples are used for the prediction
accuracy =  (test_data[test_data['predict'] > 0]['predict'].count() / float(test_data['predict'].count()))
print 'Good Samples Accuracy: ' + str(round(accuracy,2))



# Check the Bad Samples Accuracy
test_data = pd.read_csv('bad_samples.csv',sep=',')
test_labels          = test_data['labels']
test_features        = test_data.values
test_data['predict'] = et.predict(test_features)


accuracy =  (test_data[test_data['predict'] < 1]['predict'].count() / float(test_data['predict'].count()))
print 'Bad Samples Accuracy: ' + str(round(accuracy,2))




# Save the model as a pickle file
from sklearn.externals import joblib
joblib.dump(et, 'image_quality_seggregator.pkl') 

