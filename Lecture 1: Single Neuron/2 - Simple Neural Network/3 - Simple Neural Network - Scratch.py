architecture = [3, 5, 4, 2]

import torch

# input Data
X = torch.Tensor( [+1.2, -5.1, +2.1] )

# hidden layer 1
z1 = torch.dot(x1, w1.T) + b1
y1 = torch.nn.relu( z1 )

# hidden layer 2
x2 = y1 # output of layer 1 -> input of layer 2
z2 = torch.dot(x2, w2.T) + b2
y2 = torch.nn.relu( z2 )

# output layer
x3 = y2 # output of layer 2 -> input of layer 3
z3 = torch.dot(x3, w3.T) + b3
y_hat = torch.exp( z3 ) / 			\
		torch.sum( torch.exp(z3) )
