Synapse = Connection = One Parameter at each Synapse

Brain as NN
1. Neurons                              = 88 million
2. Connections / Synapses / Parameters  = 10k per neuron
3. 1 synapse                            = Each synapse can store a small amount of information.
5. Total sypanses                       = 100 to 1000 trillion synapse
6. Total Parameters                     = 100 trillion
7. Learning Algorithm: Many learning algorithms simultaniously, with much efficient learning rate.
8. High Parallelization
9. More complex types neurons
10. More complex neurotransmittors at synapse
11. More complex hormones affecting brain networks


4. 1 Connection = Learned Hardcoded Information. Connection -> Brain Wrinkle
5. Learn what? Elon Musk vs Elizabeth Holmes. They both have connections but for different things. They have learned different things, even though they are both represented by neuron connection
4. Synapse vs RAM. very small and very low power memory access.


$$
\forall_{\ k\ =\ l0}^{\ k\ =\ layers}\\
    \hspace{25mm}       \forall_{\ j=0}^{\ j=nerons} nn_{[k][j]} \\
        \hspace{50mm}       \sum_{i=0}^{i=\ columns} X_{[i]} \odot W_{[k][j][i]}
$$
```python

for layer_no,layer in enumerate(layers):
    for neuron_no,neuron in enumerate(neurons):
        z[neuron_no] = 0
        for connection_no, connection in enumerate(neuron):
            z[neuron_no] = z[neuron_no] + 
            ( 
                X[connection_no] 
                * W[layer_no][neuron_no][connection_no] 
                
                + b[layer_no][neuron_no]
            )
            a[neuron_no] = activation(z[neuron_no])


```