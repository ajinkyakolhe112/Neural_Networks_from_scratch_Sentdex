inputs = [+1.2, -5.1, +2.1]
X = inputs

weights = [+3.1, -2.1, +8.7]
bias = 3.0
W = (weights, bias)

# Weighted Sum
# w[0] = + 3.1
# w[1] = - 2.1
# w[2] = +8.7
weighted_sum = \
  inputs[0] * weights[0] + \
  inputs[1] * weights[1] + \
  inputs[2] * weights[2]

output = weighted_sum + bias
