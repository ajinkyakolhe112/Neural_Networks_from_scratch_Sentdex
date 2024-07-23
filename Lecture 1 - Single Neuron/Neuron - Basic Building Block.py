#%
# 1 Neuron in 1st Hidden Layer
inputs  = [ 1   , 2   , 3    ]
weights = [ 0.2 , 0.8 , -0.5 ] # 1st Neuron in Hidden Layer 1
bias    =   2

output_1 = (inputs[0] * weights[0]) + (inputs[1] * weights[1]) + (inputs[2] * weights[2]) + bias

print(output)

#%
import keras
model = keras.Sequential([
  # Single Neuron in a Layer
  keras.layers.Input(input_size = (3,)),
  keras.layers.Dense(units = 1, activation="relu"),
])

#%
import torch
torch.nn.Linear(in_features = 3 , out_features = 1) # Fully Connect Neuron