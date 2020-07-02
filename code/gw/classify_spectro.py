
import pandas as pd
from keras import layers
from keras import models
from keras.utils import to_categorical
import os
import numpy as np


# load the dataset
image_file='/home/osboxes/Documents/bigdata-workshop-es/dataset/gw_%s_images.npy'
labels_file='/home/osboxes/Documents/bigdata-workshop-es/dataset/gw_%s_labels.npy'

SHAPE_SIZE_X = 140
SHAPE_SIZE_Y = 170

images = np.load(image_file % "train", allow_pickle=True)
labels = np.load(labels_file % "train")

#Designing the right model for the classification of the spectrograms
model = models.Sequential()

model.add(layers.Conv2D(32,(3,3), activation="relu", input_shape=(SHAPE_SIZE_X,SHAPE_SIZE_Y,1)))
model.add(layers.MaxPooling2D(2,2))
model.add(layers.Conv2D(64,(3,3), activation="relu"))
model.add(layers.MaxPooling2D(2,2))
model.add(layers.Conv2D(64,(3,3), activation="relu"))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(2, activation='softmax'))

model.summary()

# train the recurrent neural network

#images = images.astype('float32')/255

model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(images, labels, epochs=5, batch_size=64)

# load the test set

images = np.load(image_file % "test")
labels = np.load(labels_file % "test")
#images = images.astype('float32')/255

test_loss, test_acc = model.evaluate(images, labels)

print("Convolutional Network model LOSS: %d" % test_loss)
print("Convolutional Network model ACCURACY: %d" % test_acc)

# predict the test set



