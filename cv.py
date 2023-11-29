import cv2
import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, Dropout
from tensorflow.keras.utils import to_categorical
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
data = pd.read_csv("churn.csv")

data['Churn'] = le.fit_transform(data['Churn'])

for i in data.columns:
    if data[i].dtype == 'object':
        data[i] = le.fit_transform(data[i])
print(data.head())
predictors = data.drop(['customerID','Churn'], axis=1).values
predictors = predictors.astype('float32')
print(predictors)
n_cols = predictors.shape[1]
target = to_categorical(data['Churn'])
model=Sequential()
model.add(Dense(1000, activation='relu', input_shape=(n_cols,)))
model.add(Dense(1000, activation='relu'))
model.add(Dense(500, activation='relu'))
model.add(Dense(100, activation='relu'))
model.add(Dense(2, activation='softmax'))
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(predictors,target, epochs=20)