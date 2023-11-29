import pandas as pd
import numpy as np
from tensorflow import one_hot
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, Dropout
from tensorflow.keras.utils import to_categorical,image_dataset_from_directory

from sklearn.preprocessing import LabelEncoder
import cv2
import tensorflow as tf
print(tf.config.list_physical_devices('GPU'))