architecture = [3, 5, 4, 2]

import torch

# input Data
X =  Torch.Tensor([+1.2, -5.1, +2.1])

model = torch.nn.Sequential(
  
  # hidden layer 1
  nn.Linear(in_features= 3, out_features= 4), nn.ReLU(),
  
  # hidden layer 2
  nn.Linear(in_features= 4, out_features= 4), nn.ReLU(),
  
  # output layer
  nn.Linear(in_features= 4, out_features= 2), nn.Softmax(),
)

# forward pass
model(X)