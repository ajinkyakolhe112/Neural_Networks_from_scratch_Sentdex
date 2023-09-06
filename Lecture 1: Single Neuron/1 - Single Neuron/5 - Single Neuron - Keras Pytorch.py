import numpy as np
X = np.array([ +1.2, -5.1, +2.1 ])
X = X.reshape(1,3)

import tensorflow as tf
from tensorflow import keras
import torch

neuron_tf = keras.layers.Dense (units = 1      , input_shape=[3])
neuron_pt = torch.nn.Linear    (in_features = 3, out_features = 1)

# Forward Pass
output = neuron_tf( tf.convert_to_tensor(X)  )
output = neuron_tf( torch.Tensor(X)          )



