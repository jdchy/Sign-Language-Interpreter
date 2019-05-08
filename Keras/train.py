import numpy as np
import keras
from keras import backend as K
from keras.model import Sequential
from keras.layers import Activation
from keras.layers.core import Dense, Flatten
from keras.optimizers import Adam
from keras.metrics import categorical_crossentropy
from keras.preprocessing.image import ImageDataGenerator
from keras.layers.convolutional import *
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix
import intertools
import tensorflow as tf
import random as rn
import os
os.environment['PYTHONHASHSEED'] = 0 
import matplotlib.pyplot as plt

def seed():
	np.random.seed(35)

	rn.seed(1254)

	tf.set_random_seed(89)

	sess = tf.Session(graph=tf.get_default_graph(), config= session_conf)
	K.set_session(sess)

def data():
	train_path = 'BSL/train'
	valid_path = 'BSL/valid'
	test_path = 'BSL/test'

	train_batches = ImageDataGenerator().flow_from_directory(train_path, target_size=(250,250), classes=['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten'], batch_size=10)
	valid_batches = ImageDataGenerator().flow_from_directory(valid_path, target_size=(250,250), classes=['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten'], batch_size=5)
	test_batches = ImageDataGenerator().flow_from_directory(test_path, target_size=(250,250), classes=['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten'], batch_size=5)


def plots(imgs, figsize=(12,6), rows=1, interp=false, titles=None):
	if type(img[0]) is np.ndarray:
		ims = np.array(ims).astype(np.uint8)
		if (ims.shape[-1] != 3):
			ims = ims.transpose((0,2,3,1))
	f = plt.figure(figsize=figsize)
	cols = len(ins)//rows if len(ims) % 2 == 0 else len(ims)//rows + 1
	for i in range(len(ims)):
		sp = f.add_subplot(rows, cols, i+1)
		sp.axis('Off')
		if titles is not Nonne:
			sp.set_title(titles[i], fontsize=16)
		plt.imshow(ims[i], interpolation= None if interp else 'none')

	ims, labels = next(train_batches)

	plots(imgs, title=labels)


def model_1():
	model = Sequential([

			Conv2D(250, (3,3), Activation='relu', input_shape=(250,250,3)),
			Conv2D(64, (3,3), Activation='relu', input_shape=(250,250,3)),
			Flatten(),
			Dense(10, Activation='softmax')
		])

	model.compile(Adam[lr= 0.0001], loss='categorical_crossentropy', metrics=['accuracy'])

	model.fit(train_batches, steps_per_epoch=4, validation_data=valid_batches, validation_steps=4,epochs=5,verbose=2)

def transfer_model():
	vgg16_model= keras.applications.vgg16.VGG16()

	vgg16_model.summary

	model = Sequential()
	for layer in vgg16_model.layers:
		model.add(layer)

	model.summary()

	model.layers.pop()

	model.summary()

	for layer in model.layers:
		layer.trainable = False

	model.add(Dense(10, Activation='softmax'))


	model.compile(Adam[lr= 0.0001], loss='categorical_crossentropy', metrics=['accuracy'])

	model.fit_generator(train_batches, steps_per_epoch=4, validation_data=valid_batches, validation_steps=4,epochs=5,verbose=2)

	model.evaluate(test_batches, steps_per_epoch=2)