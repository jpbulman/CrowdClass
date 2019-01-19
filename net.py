import cv2
import numpy as np
import os
from random import shuffle
import tensorflow as tf
from tqdm import tqdm
#import matplotlib.pyploy as plt
from keras.models import Sequential
from keras.layers import *
from keras.optimizers import *

train_data = 'Images/Train'
test_data = 'Images/Test'

def get_label(img):
	label = img.split('.')[0]
	if label == 'choc':
			return np.array([1,0])
	elif label == 'oat':
			return np.array([0,1])
	print("oh shoot oh shoot oh shoot what happened")
	return

def get_train_data():
	images = []
	for i in tqdm(os.listdir(train_data)):
		path = os.path.join(train_data, i)
		img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
		img = cv2.resize(img, (128, 128))
		print("test!")
		cv2.imwrite('/Images/Blorp/' + str(i) + '.png', img)
		images.append([np.array(img), get_label(i)])
	shuffle(images)
	return images

def get_test_data():
	images = []
	for i in tqdm(os.listdir(test_data)):
		path = os.path.join(train_data, i)
		img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
		img = cv2.resize(img, (128, 128))
		images.append([np.array(img), get_label(i)])
	shuffle(images)
	return images

get_train_data()
