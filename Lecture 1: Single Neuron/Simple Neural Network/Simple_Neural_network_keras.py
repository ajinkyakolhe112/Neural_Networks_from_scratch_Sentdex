#%%
# NN = [ Input , 4, 4, Output 2 ]
from tensorflow import keras

input_layer     = keras.layers.Input( shape=2 )
output_layer    = keras.layers.Dense( units=2 , activation="softmax")

hidden_layers   = [
                    keras.layers.Dense(units = 4), 
                    keras.layers.Dense(units = 4)
                ]
#%%
model = keras.model.Sequential([
    input_layer,
    hidden_layers[0],
    hidden_layers[1],
    output_layer,
])

import torch
import torch.nn as nn
hidden_layers = [
    nn.Linear(in_features = 2, out_features= 4),
    nn.Linear(4, 4),
]
output_layer = nn.Linear(in_features = 4, out_features= 2)