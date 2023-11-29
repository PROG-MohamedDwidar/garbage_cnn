#import cv2
import pandas as pd
import numpy as np
from tensorflow import one_hot
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, Dropout
from tensorflow.keras.utils import to_categorical,image_dataset_from_directory

from sklearn.preprocessing import LabelEncoder




data = image_dataset_from_directory("GarbageData")
data = data.shuffle(100)
data = data.map(lambda x, y: (x/255.0, one_hot(y, depth=6)))

data_itr = data.as_numpy_iterator()
batch = data_itr.next()

train_size = int(len(data)*0.7)
test_size = int(len(data)*0.1)+1
val_size = int(len(data)*0.2)+1

train = data.take(train_size)
val = data.skip(train_size).take(val_size)
test = data.skip(train_size+val_size).take(test_size)

print(train_size,test_size,val_size)

model=Sequential()
model.add(Conv2D(25,kernel_size=3, activation='relu', input_shape=(256,256,3),padding="same"))
model.add(MaxPooling2D())
model.add(Conv2D(100,kernel_size=3, activation='relu'))
model.add(MaxPooling2D())
model.add(Conv2D(25 ,kernel_size=3, activation='relu'))
model.add(MaxPooling2D())
model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dense(6, activation='softmax'))
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])


model.fit(train, epochs=20,validation_data=val)


model.predict()