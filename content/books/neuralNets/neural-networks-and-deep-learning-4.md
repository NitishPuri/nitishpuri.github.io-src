---
title: A visual proof that neural networks can compute any function
author: Micheal Nelson
tags: deep-learning, notes
series: Neural Networks and Deep Learning
summary: Neural Networks and Deep Learning, Chapter 4
date: 2017-11-23
---
Notes for the [book](http://neuralnetworksanddeeplearning.com/index.html).   
[Source code](https://github.com/mnielsen/neural-networks-and-deep-learning) for the book.


## **Chapter 4: A visual proof that neural networks can compute any function**

One of the most striking facts about neural networks is that they can compute any function at all.   
That is, suppose someone hands you some complicated, wiggly function, $f(x)$:   
![alt](/images/nnfordl/4_fun1.png)   

No matter what the function, there is guaranteed to be a neural network so that for every possible input, $x$, the value $f(x)$ (or some close approximation) is output from the network.   
This result holds even if the function has many inputs,   
![alt](/images/nnfordl/4_fun2.png)   

This result tells us that neural networks have a kind of universality. No matter what function we want to compute, we know that there is a neural network which can do the job.   

What's more, this universality theorem holds even if we restrict our networks to have just a single layer intermediate between the input and the output neurons - a so-called single hidden layer. So even very simple network architectures can be extremely powerful.   

However, the proofs for the universality of neural networks is not widely understood and the explanations are quite technical. Here we attempt to simplify the underlying intuition.   

Any process that we can do or imagine can be thought of as a function computation. Universality means that neural networks can do all these things, and many more.   

So, we know neural networks can compute things, but to find those networks we need learning algorithms!!   

### Two Caveats










