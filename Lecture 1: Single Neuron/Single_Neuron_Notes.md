$$
\begin{align*}
X_{example} \ &= \begin{bmatrix} x_{1}\\x_{2}\\x_{3}\\ \vdots\\ x_{n}\\\end{bmatrix}\\
Weights_{neuron} &= \begin{bmatrix} w_{1}\\w_{2}\\w_{3}\\ \vdots\\ w_{n}\\\end{bmatrix}\\
z\ &= X_{input} \odot Weights + bias      \\
a\ &= \sigma(z)                           \\
X_{transformed}\ &= \begin{bmatrix} a_{1} \\ a_{2} \\ a_{3} \vdots \\ a_{neurons}\end{bmatrix}\\
\end{align*}
$$

```python
from tensorflow import keras

X_actual, Y_actual = training_data

model = keras.models.Sequential([
    keras.layers.Input(shape = 3 ),                         # special input layer
    keras.layers.Dense(units = 4 ),
    keras.layers.Dense(units = 4 ),
    keras.layers.Dense(units = 2  , activation="softmax"),  # output layer
])

Y_predicted = model(X_actual) # model( X_actual, Weights )
loss        = keras.losses.CategoricalCrossEntropy(Y_predicted,Y_actual) # loss -> Y_predicted -> Weights

model.fit(X_actual, Y_actual, epochs = 10)
```
