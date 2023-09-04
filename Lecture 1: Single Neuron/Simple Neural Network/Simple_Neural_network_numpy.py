import numpy as np

# NN = [Input, 4, 4, 2 ]


def Neuron_Transformation(X, W, b, activation):
    z = np.dot(X,W.T) + b
    a = activation(z)
    return a

X
y1     = Neuron_Transformation(X , w1, b1)
y2     = Neuron_Transformation(y1, w2, b2 )

y_pred       = Neuron_Transformation(y3, w3, b3)
y_pred_probs = np.exp(y_pred)               \
                /                           \
                np.sum( np.exp(y_pred) )
                
loss   = -np.log(np.sum(y * y_pred_probs))