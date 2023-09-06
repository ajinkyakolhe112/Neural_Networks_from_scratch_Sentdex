inputs = [+1.2, -5.1, +2.1]

class Neuron:
  weights = [+3.1, -2.1, +8.7]
  bias = 3.0
  W = (weights, bias)
  
  def forward_pass( X ):
    output = X[0]*weights[0] + \
             X[1]*weights[1] + \
             X[2]*weights[2]   \
             + bias
    return output

output = Neuron.forward_pass(inputs)