Single Neuron
- Input = $[\ +1.2, -5.1, +2.1\ ]$
- 3 Incoming Connections & 3 *Corresponding* Weights for each incoming connection
$$
\begin{align*}
\\
X_{example} \ &= \begin{bmatrix} x_{0} & x_{1} & x_{2}\end{bmatrix} \tag{1. Data}\\
W_{neuron}    &= \begin{bmatrix} w_{0}\\w_{1}\\w_{2}\end{bmatrix} \tag{2. Weights}\\
z_{0}\        &= X_{input} \odot W + bias    \tag{3. Dot Product}         \\
a_{0}\        &= \sigma(z_{0}) \tag{4. Activation}                       \\
X_{new}\      &= \begin{bmatrix} a_{0}\\ \end{bmatrix}\\
\\
X.shape &= 1 \times 3\\
W.shape &= 3 \times 1
\\
\end{align*}
$$