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
%matplotlib inline

def seed(n):
	np.random.seed(n)

	rn.seed(1254)

	tf.set_random_seed(89)

	sess = tf.Session(graph=tf.get_default_graph(), config= session_conf)
	K.set_session(sess)

def data():
	train_path = 'BSL/train'
	valid_path = 'BSL/valid'
	test_path = 'BSL/test'

	train_batches = ImageDataGenerator().flow_from_directory(train_path, target_size=(150,250), classes=['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten'], batch_size=10)
	valid_batches = ImageDataGenerator().flow_from_directory(valid_path, target_size=(150,250), classes=['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten'], batch_size=10)
	test_batches = ImageDataGenerator().flow_from_directory(test_path, target_size=(150,250), classes=['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten'], batch_size=10)

def transfer_model():
	model = keras.applications.mobilenet.MobileNet()

	model.summary()


	for layer in model.layers:[-23]
		layer.trainable = False

	model.add(Dense(10, Activation='softmax'))


	model.compile(Adam[lr= 0.0001], loss='categorical_crossentropy', metrics=['accuracy'])

	model.fit_generator(train_batches, steps_per_epoch=80, validation_data=valid_batches, validation_steps=10,epochs=100,verbose=2)

	test_labels= test_batches.classes


	predictions = model.predict_generator(test_batches, steps=10, verbose=0)

	cm = confusion_matrix(test_labels,predictions.argmax(axis=1))
	test_batches.class_indices 

	cm_plot_labels = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']
	plot_confusion_matrix(cm, cm_plot_labels,title='Confusion Matrix')
	model.evaluate(test_batches, steps_per_epoch=2)