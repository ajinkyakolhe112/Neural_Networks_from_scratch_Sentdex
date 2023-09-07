architecture = [3, 5, 4, 2]

import tensorflow as tf
from tensorflow import keras

# input Data
X =  tf.Tensor([+1.2, -5.1, +2.1], dtype=float32)

model = keras.models.Sequential([
  # input layer
  keras.layers.Input(3), 
  
  # hidden layer 1
  keras.layers.Dense(units = 4, activation="relu"),
  # hidden layer 2
  keras.layers.Dense(units = 4, activation="relu"),
  
  # output layer
  keras.layers.Dense(units = 2, activation="softmax"),
])

# forward pass
model(X)