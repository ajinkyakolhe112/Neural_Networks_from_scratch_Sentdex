#%
inputs  = [ 1   , 2   , 3    ]
weights = [ 0.2 , 0.8 , -0.5 ] # 1st Neuron in Hidden Layer 1
bias    =   2

output_1 = (inputs[0] * weights[0]) + (inputs[1] * weights[1]) + (inputs[2] * weights[2]) + bias

print(output)

#%
import keras
model = keras.Sequential([
  # Single Neuron in a Layer
  keras.layers.Dense(1, input_shape = (3), activation="relu"),
])