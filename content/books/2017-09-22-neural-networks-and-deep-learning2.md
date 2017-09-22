---
title: How the backpropogation algorithm works
author: Micheal Nelson
tags: deep-learning, notes
series: Neural Networks and Deep Learning
summary: Neural Networks and Deep Learning, Chapter 2
---
Notes for the [book](http://neuralnetworksanddeeplearning.com/index.html).   
[Source code](https://github.com/mnielsen/neural-networks-and-deep-learning) for the book.


## Chapter 2: How the backpropogation algorithm works

Was introduced in the 70's, but came into light with [this paper](https://www.nature.com/nature/journal/v323/n6088/pdf/323533a0.pdf).   

Today, it is the workhorse of learning in neural networks.   

### Warm up: a fast matrix-based approach to computing the output from a neural network

First, the notations,   
For weights,   
![alt](/images/nnfordl/backprop1.png)   

For biases and activations,   
![alt](/images/nnfordl/backprop2.png)   


These are related,   
$$\begin{eqnarray} 
  a^{l}_j = \sigma\left( \sum_k w^{l}_{jk} a^{l-1}_k + b^l_j \right),
\tag{23}\end{eqnarray}$$

which can be rewritten in *vectorized* form as,   
$$\begin{eqnarray} 
  a^{l} = \sigma(w^l a^{l-1}+b^l).
\tag{25}\end{eqnarray}$$

This form is more compact and practical as we will be using libraries that provide fast matrix multiplication and vectorization capabilities.   

### The two assumptions we need about the cost function

The goal of backpropogation is to calculate the partial derivatives $\partial C / \partial w$ and $\partial C / \partial b$.   

Here is an example of cost function we will be using(there can and will be others).   
$$\begin{eqnarray}
  C = \frac{1}{2n} \sum_x \|y(x)-a^L(x)\|^2,
\tag{26}\end{eqnarray}$$

Now, the assumptions,   

1. The cost function can be written as an average $C = \frac{1}{n} \sum_x C_x$ over cost $C_x$ for individual training examples.   
2. The cost function can be written as  a function of the outputs from the neural network:
![alt](/images/nnfordl/backprop3.png)   

$$\begin{eqnarray}
  C = \frac{1}{2} \|y-a^L\|^2 = \frac{1}{2} \sum_j (y_j-a^L_j)^2,
\tag{27}\end{eqnarray}$$


### The Hadamard product, $s \odot t$

$s \odot t$ represents the *elementwise* product of two vectors.   
$$\begin{eqnarray}
\left[\begin{array}{c} 1 \\ 2 \end{array}\right] 
  \odot \left[\begin{array}{c} 3 \\ 4\end{array} \right]
= \left[ \begin{array}{c} 1 * 3 \\ 2 * 4 \end{array} \right]
= \left[ \begin{array}{c} 3 \\ 8 \end{array} \right].
\tag{28}\end{eqnarray}$$


### The four fundamental equations behind backpropagation

First, we define the *error* in the $j^{th}$ neuron in the $l^{th}$ layer, $\delta^l_j$   
$$\begin{eqnarray} 
  \delta^l_j \equiv \frac{\partial C}{\partial z^l_j}.
\tag{29}\end{eqnarray}$$

**An equation for the error in the output layer,** $\delta^L$:   
$$\begin{eqnarray} 
  \delta^L_j = \frac{\partial C}{\partial a^L_j} \sigma'(z^L_j).
\tag{BP1}\end{eqnarray}$$

Which can again be rewritten in vectorized form,   
$$\begin{eqnarray} 
  \delta^L = \nabla_a C \odot \sigma'(z^L).
\tag{BP1a}\end{eqnarray}$$

where, in case of a quadratic cost function, we have $\nabla_a C = (a^L-y)$.So,    
$$\begin{eqnarray} 
  \delta^L = (a^L-y) \odot \sigma'(z^L).
\tag{30}\end{eqnarray}$$

**An equation for the error $\delta^l$ in terms of the error in the next layer,** $\delta^{l+1}$:   
$$\begin{eqnarray} 
  \delta^l = ((w^{l+1})^T \delta^{l+1}) \odot \sigma'(z^l),
\tag{BP2}\end{eqnarray}$$

Suppose we know the error $\delta^{l+1}$ at the $l+q^{\rm th}$ layer. When we apply the transpose weight matrix, $(w^{l+1})^T$, we can think intuitively of this as moving the error *backward* through the network, giving us some sort of measure of the error at the output of the $l^{\rm th}$ layer.   

By combining $(BP1)$ and $(BP2)$, we can compute the error $\delta^l$ for any layer in the network.   

**An equation for the rate of change of the cost with respect to any bias in the network**   

$$\begin{eqnarray}  \frac{\partial C}{\partial b^l_j} =
  \delta^l_j.
\tag{BP3}\end{eqnarray}$$







