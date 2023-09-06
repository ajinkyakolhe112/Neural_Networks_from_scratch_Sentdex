architecture = [3, 4, 4, 2]

import torch

# input Data
X =  Torch.Tensor([+1.2, -5.1, +2.1])

model = torch.nn.Sequential(
  nn.Linear(in_features= 3, out_features= 4), nn.ReLU(),
  nn.Linear(in_features= 4, out_features= 4), nn.ReLU(),
  nn.Linear(in_features= 4, out_features= 2), nn.Softmax(),
)

# forward pass
model(X)