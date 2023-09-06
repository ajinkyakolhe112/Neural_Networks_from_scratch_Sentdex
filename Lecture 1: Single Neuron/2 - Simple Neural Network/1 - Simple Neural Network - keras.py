architecture = [3, 4, 4, 2]

import tensorflow as tf
from tensorflow import keras

# input Data
X =  tf.Tensor([+1.2, -5.1, +2.1], dtype=float32)

model = keras.models.Sequential([
  keras.layers.Input(3), # input layer
  keras.layers.Dense(units = 4, activation="relu"),    # hidden layer 1
  keras.layers.Dense(units = 4, activation="relu"),    # hidden layer 2
  keras.layers.Dense(units = 2, activation="softmax"), # output layer
])

# forward pass
model(X)