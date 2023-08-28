#%%
import numpy as np

first_example = inputs[0]    # ROW MAJOR BATCH
first_neuron  = weights[0]   # ROW MAJOR WEIGHTS
first_neuron  = weights.T[0] # COLUMN MAJOR WEIGHTS
z = np.dot(inputs, weights.T) + biases

# why np array. Because data structure is list. Its not matrix. Doesn't have matrix functions like Transpose ... etc
inputs  = np.array( [    [ 1.0 , 2  , 3 , 2.5   ],
                         [ 5 , 5  , 6 , 2     ],
                    ])  
weights = np.array( [   [0.1, -3.2  , 0.9   , 0.2   ],
                        [2  , 0.2   , 3.2   , -5    ],
                        [0  ,   0   ,   0   , 10    ],
                        [5  , 5     , 0     , 0     ],
                        [0.24,  0.25, 0.25  , 0.25  ] 
                    ]) 
biases  = np.array( [
                        1,
                        2,
                        3,
                        4,
                        5
                    ])

no_neurons = 4
inputs_shape  = (2,4)
weights_shape = (5,4) # each weight parameter = (1,4). each weight parameter is a vector. 
biases_shape  = (1,5)


# each dot product is weighted average of the input_data
z1 = np.matmul   (inputs,weights.T)  + biases     # 2*4 , 4*5 + bias = 5,1
z2 = np.dot      (inputs,weights.T)  + biases     # 2*4 , 4*5 + bias = 5,1
z1 = np.matmul   (inputs,weights.T)  + biases.T   # 2*4 , 4*5 + bias = 1,5
z2 = np.dot      (inputs,weights.T)  + biases.T   # 2*4 , 4*5 + bias = 1,5
try:
    # Error for Multi Batch Input, but works for Single
    z3 = np.matmul   (weights,inputs)    + biases   # 5*4 , 2*4
    z4 = np.dot      (weights,inputs)    + biases   # 5*4 , 2*4

    # Error for Single
    z5 = np.matmul   (inputs,weights)    + biases
    z6 = np.dot      (inputs, weights)   + biases
except ValueError as e:
    print("Shape Error")
print("END")

#%%


no_neurons    = int(np.random.randint(1,100, size=(1)))
data_points   = 10
data_dims     = 4

inputs  = np.round( np.random.randn(data_points, data_dims), 2 )
weights = np.round( np.random.randn(no_neurons , data_dims), 2 )
biases  = np.round( np.random.randn(no_neurons , 1        )  , 2 )

# Newer way
default_random_number_generator = np.random.default_rng()
default_random_number_generator.integers(100, size=(1))
default_random_number_generator.normal(loc = 2,scale = 3, size=1)

#%%

z = np.dot(inputs, weights.T) + biases
a = np.maximum(0,z)

A = [a_0, a_1, ... , a_n ]
output = A
output_normalized = np.normalize(A)
input_transformed = output_normalized

# activation function y = max(0,x)