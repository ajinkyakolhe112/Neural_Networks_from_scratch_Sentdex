$$
\begin{align*}
\\
X_{example} \ &= \begin{bmatrix} x_{0} & x_{1} & x_{2}\end{bmatrix}\\
W_{neuron}    &= \begin{bmatrix} w_{0}\\w_{1}\\w_{2}\end{bmatrix}\\
z_{0}\        &= X_{input} \odot W + bias             \\
a_{0}\        &= \sigma(z_{0})                        \\
X_{new}\      &= \begin{bmatrix} a_{0}\\ \end{bmatrix}\\
\\
X.shape &= 1 \times 3\\
W.shape &= 3 \times 1
\\
\end{align*}
$$