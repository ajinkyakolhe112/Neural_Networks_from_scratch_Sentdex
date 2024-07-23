$$
\begin{align*}
\\
X_{example} \ &= \begin{bmatrix} x_{0} & x_{1} & x_{2}\end{bmatrix} \tag{1. Data}\\
W_{neuron}    &= \begin{bmatrix} w_{0}\\w_{1}\\w_{2}\end{bmatrix} \tag{2. Weights}\\
z_{0}\        &= X_{input} \odot W + bias    \tag{3. Dot Product}         \\
z_{0}\        &= \begin{bmatrix} x_{0} & x_{1} & x_{2}\end{bmatrix} \odot \begin{bmatrix} w_{0}\\w_{1}\\w_{2}\end{bmatrix} + bias    \tag{3. Dot Product}         \\
a_{0}\        &= \sigma(z_{0}) \tag{4. Activation}                       \\
\end{align*}
$$