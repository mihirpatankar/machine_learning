#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import numpy as np
### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#slicing the training set

#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 



#########################################################
### your code goes here ###
clf = SVC(C=10000.0,kernel="rbf")
clf.fit(features_train,labels_train)
pred=clf.predict(features_test)
print accuracy_score(pred, labels_test)
#predictions for 10th, 26th and 50th test data
#print pred[10]
#print pred[26]
#print pred[50]

#number of elements predicted as Chris(1)
print list(pred).count(1)
#########################################################


