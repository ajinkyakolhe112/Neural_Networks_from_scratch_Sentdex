inputs    = [1  , 2  , 3   ]

# 4 Neurons in 1st Hidden Layer
weights_1 = [0.2, 0.8, -0.5]
weights_2 = [0.2, 0.8, -0.5]
weights_3 = [0.2, 0.8, -0.5]
weights_4 = [0.2, 0.8, -0.5]
bias_1    = 2
bias_2    = 2
bias_3    = 2
bias_4    = 2

output_1 = (inputs[0] * weights_1[0]) + (inputs[1] * weights_1[1]) + (inputs[2] * weights_1[2]) + bias_1
output_2 = (inputs[0] * weights_2[0]) + (inputs[1] * weights_2[1]) + (inputs[2] * weights_2[2]) + bias_2
output_3 = (inputs[0] * weights_3[0]) + (inputs[1] * weights_3[1]) + (inputs[2] * weights_3[2]) + bias_3
output_4 = (inputs[0] * weights_4[0]) + (inputs[1] * weights_4[1]) + (inputs[2] * weights_4[2]) + bias_4

output   = [output_1, output_2, output_3, output_4]
print(output) # 4 Neurons, output a vector of 4 dimentions.

import keras
model = keras.Sequential([
  # Hidden Layer 1
  keras.layers.Dense(units = 4, input_shape = (3,), activation="relu"),
])
model.summary()

import torch
import torchinfo

layer = torch.nn.Linear(in_features = 7, out_features = 4)
torchinfo.summary(layer, input_size=(7,), verbose = 2, col_names=["input_size", "output_size", "kernel_size", "num_params", "params_percent"])