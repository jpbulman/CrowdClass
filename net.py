import cv2
import numpy as np
import os
from random import shuffle
import tensorflow as tf
from tqdm import tqdm
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import *
from keras.optimizers import *

IMAGE_SIZE = 200
IMAGE_SIZE_DISPLAY = 512

train_data = 'Images/Train'
test_data = 'Images/Test'
demo_data = 'Images/Demo'

def get_label(img):
	label = img.split('.')[0]
	if label == 'choc':
			return np.array([1,0])
	elif label == 'oat':
			return np.array([0,1])
	print("oh shoot oh shoot oh shoot what happened")
	return

def grab_data_from(imgDir):
	images = []
	for i in tqdm(os.listdir(imgDir)):
		path = os.path.join(imgDir, i)
		img = cv2.imread(path)#, cv2.IMREAD_GRAYSCALE)
		img = cv2.resize(img, (IMAGE_SIZE, IMAGE_SIZE))
		images.append([np.array(img), get_label(i)])
	shuffle(images)
	return images

'''
def grab_data_from_rgb(imgDir):
	images = []
	for i in tqdm(os.listdir(imgDir)):
		path = os.path.join(imgDir, i)
		img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
		img = cv2.resize(img, (IMAGE_SIZE_DISPLAY, IMAGE_SIZE_DISPLAY))
		images.append([np.array(img), get_label(i)])
	shuffle(images)
	return images
'''

training_pics = grab_data_from(train_data)
testing_pics = grab_data_from(test_data)
demo_pics = grab_data_from(demo_data)

#testing_pics_rgb = grab_data_from_rgb(test_data)

tr_img_data = np.array([i[0] for i in training_pics]).reshape(-1,IMAGE_SIZE,IMAGE_SIZE,3)
tr_lbl_data = np.array([i[1] for i in training_pics])

tr_img_data = np.array([i[0] for i in testing_pics]).reshape(-1,IMAGE_SIZE,IMAGE_SIZE,3)
tr_lbl_data = np.array([i[1] for i in testing_pics])

model = Sequential()

model.add(InputLayer(input_shape = [IMAGE_SIZE,IMAGE_SIZE,3]))

# Convolution layer 1
model.add(Conv2D(filters = 32, kernel_size = 5, strides = 1, padding = 'same', activation = 'relu'))
model.add(MaxPool2D(pool_size = 5, padding = 'same'))

# Convolution layer 2
model.add(Conv2D(filters = 50, kernel_size = 5, strides = 1, padding = 'same', activation = 'relu'))
model.add(MaxPool2D(pool_size = 5, padding = 'same'))

# Convolution layer 3
model.add(Conv2D(filters = 80, kernel_size = 5, strides = 1, padding = 'same', activation = 'relu'))
model.add(MaxPool2D(pool_size = 5, padding = 'same'))


# Convolution layer 4
model.add(Conv2D(filters = 80, kernel_size = 5, strides = 1, padding = 'same', activation = 'relu'))
#model.add(MaxPool2D(pool_size = 5, padding = 'same'))

# Convolution layer 5
model.add(Conv2D(filters = 80, kernel_size = 5, strides = 1, padding = 'same', activation = 'relu'))
model.add(MaxPool2D(pool_size = 5, padding = 'same'))

# Convolution layer 6
model.add(Conv2D(filters = 80, kernel_size = 5, strides = 1, padding = 'same', activation = 'relu'))
#model.add(MaxPool2D(pool_size = 5, padding = 'same'))


model.add(Dropout(0.3))
model.add(Flatten())
model.add(Dense(512, activation = 'relu'))
model.add(Dropout(rate = 0.5))
model.add(Dense(2, activation = 'softmax'))
optimizer = Adam(lr = 1e-3)

model.compile(optimizer = optimizer, loss = 'categorical_crossentropy', metrics = ['accuracy'])
model.fit(x = tr_img_data, y = tr_lbl_data, epochs = 40, batch_size = 40)
model.summary()

fig = plt.figure(figsize = (14, 14))

for cnt, data in enumerate(demo_pics):

	y = fig.add_subplot(3, 3, cnt+1)
	img = data[0]
	data = img.reshape(1, IMAGE_SIZE, IMAGE_SIZE, 3)
	model_out = model.predict([data])

	if np.argmax(model_out) == 1:
		str_label = 'Oat'
	else:
		str_label = 'Choc'

	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

	y.imshow(img)#, cmap = 'gray')
	plt.title(str_label)
	y.axes.get_xaxis().set_visible(False)
	y.axes.get_yaxis().set_visible(False)

plt.show()
