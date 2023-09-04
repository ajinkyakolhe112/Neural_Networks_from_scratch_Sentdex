
from loguru import logger

# Single Neuron

X_inputs    = [ 1.2, 5.1, 2.1 ]
class Neuron:
    weights     = [ 3.1, 2.6, 6.2 ]
    bias        = 3

logger.debug(f'{len(X_inputs)}, {len(Neuron.weights)}')

z = X_inputs[0] * Neuron.weights[0] + \
    X_inputs[1] * Neuron.weights[1] + \
    X_inputs[2] * Neuron.weights[2]   \
    + Neuron.bias

output = z
print(output)


from tensorflow import keras
model = keras.models.Sequential([
    keras.layers.Input(shape=(3)),
    keras.layers.Dense(units = 1, activation="relu"),
])