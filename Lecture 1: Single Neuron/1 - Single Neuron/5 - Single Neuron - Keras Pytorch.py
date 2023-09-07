import numpy as np

X = np.array( [ +1.2, -5.1, +2.1 ] )
X = X.reshape( 1,3 ) # Single Example of 3 Dimention. Format = (Number of Examples, Number of Dimentions)

import tensorflow as tf
from tensorflow import keras
import torch

# Single Neuron in Keras
neuron = keras.layers.Dense (units = 1      , input_shape=[3])
# Forward Pass
output = neuron( tf.convert_to_tensor(X)  )

# Single Neuron in Pytorch
neuron = torch.nn.Linear    (in_features = 3, out_features = 1)
# Forward Pass
output = neuron( torch.Tensor(X)          )



