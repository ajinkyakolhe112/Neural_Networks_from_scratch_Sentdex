
all_examples     = X_train,Y_train
model            = model
error = loss_function

for example in all_examples:
    x_actual, y_actual = example
    y_predicted  = imperfect_model(x)
    y_actual     = perfect_model(x_actual)    
    error_value  = error(y_predicted, y_actual)
    
#%% [markdown]
"""
$$\begin{align*}

E &= \bigl[ \sigma (X_{available} \odot W + b)\bigr]_{[layer][neurons] or [depth][width]}  - y_{available}\\\\

\frac{\partial E}{\partial W} &= \frac{\partial E}{\partial W_{layer\_1}} + \frac{\partial E}{\partial W_{layer\_2}} + \dots \frac{\partial E}{\partial W_{layer\_n}}\\

\frac{\partial E}{\partial W} &= \frac{\partial E}{\partial W_{[layer\_1][neuron\_1]}}\\
\end{align*}
\\
\begin{align*}
\nabla gradient &= \lim_{\partial W \to 0} \frac{\partial E}{\partial W}\\
automatic\_gradient &= dE\_dW\\
W &= W - \lim_{lr \to 0\ ,\ \partial W \to 0}\frac{\partial E}{\partial W}*\ (lr\ or\ step\_length)\\

\end{align*}
$$
"""
#%%