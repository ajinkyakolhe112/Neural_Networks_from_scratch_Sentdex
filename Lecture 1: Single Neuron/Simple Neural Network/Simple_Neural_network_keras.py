from tensorflow import keras

input_layer     = keras.layers.Input(shape=3)
output_layer    = keras.layers.Dense(units=2)
hidden_layers   = [
                    keras.layers.Dense(units = 4), 
                    keras.layers.Dense(units = 4)
                ]

model = keras.model.Sequential([
    input_layer,
    hidden_layers[0],
    hidden_layers[1],
    output_layer,
])