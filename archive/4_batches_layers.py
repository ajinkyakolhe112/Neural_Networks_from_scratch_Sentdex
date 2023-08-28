B,C,H,W = 60000, 3, 224,224
X = (B,C,H,W)

B,nDims = 7,3
random_generator = np.random.default_rng()
X = random_generator.uniform(B,nDims) # X = (B, nDims)


from torch.nn.functional import relu, dot

class Single_Neuron:
    def __init__(self, DIMS_neuron , operation=dot, activation_function=relu):
        num_neurons = 1
        self.weight_vector  = random_generator.uniform(DIMS_neuron)
        self.bias_vector    = random_generator.uniform(size=(num_neurons))
        self.neuron_dimentions     = self.DIMS_neuron
        # self.operation      = operation
        # self.activation_func = activation_function 

    def forward(self, example):
        x_batch, y_actual_batch = example

        y_predicted_batch = dot(x_batch,self.weight_vector.T) + self.bias_vector
        y_activated_batch = relu(y_predicted_batch)

        # y_predicted_batch = self.operation(x_batch,self.weight_vector)
        # y_activated_batch = self.activation_func(y_predicted_batch)

        return y_activated_batch

class Layer:
    def __init__(self, n_inputs, n_neurons):
        self.weights_matrix = torch.zeros(n_neurons, n_inputs) # ROW MAJOR on channel_no or neuron_no
        self.bias_vector    = torch.zeros(n_neurons)           # ROW MAJOR on channel_no or neuron_no. Neurons are vertical but their bias vector is horizontal or row vector

    def forward(self, example):
        x_train, y_train, weights_matrix, bias_vector = example, self.weights_matrix.T, self.bias_vector

        y_predicted = dot(x_train,weights_matrix) + bias_vector
        y_activated = relu(y_predicted)

        return y_activated

class Block_Layers:
    def __init__(self, n_layers:int , neurons_per_layers:[] ):
        pass
