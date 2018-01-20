---
title: Fundamentals of Computer Graphics, Part 7
author: Peter Shirley
use_math: true
tags: graphics, notes, programming
series: Fundamentals of Computer Graphics
summary: Sampling and Curves
date: 2017-11-30
---

## Chapter 14 : Sampling 

### Integration 
Although the words “integral” and “measure” often seem intimidating, they relate to some of the most intuitive concepts found in mathematics, and they should not be feared.   

For example, on the 2D real plane $R^2$, we have the area measure $A$ which assigns a value to a set of points in the plane. Note that $A$ is just a function that takes pieces of the plane and returns area. This means the 
domain of $A$ is all possible subsets of $R^2$, which we denote as the power set $P(R^2)$. Thus, we can characterize $A$ in arrow notation:   

$$\begin{align}
& A : \mathcal P(\mathbb R^2) \to \mathbb R^+. \\
& A([a, a+1]\times [b, b + 1]) = 1,
\end {align}$$   

To be considered a measure, a function has to obey certain area-like properties.   
For example, we have a function $\mu : P(S) \to R^+$. For $\mu$ to be a measure, the following conditions must be true:   

1. The measure of the empty set is zero: $\mu(\phi) = 0$,
2. The measure of two distinct sets together is the sum of their measure alone.
This rule with possible intersections is   
$$\begin{align}
\mu (A \cup B) = \mu (A) + \mu(B) − \mu(A \cup B),
\end {align}$$   
where $\mu$ is the set union operator and $\mu$ is the set intersection operator.   

When we actually compute measures, we usually use *integration*.   

$$\begin{align}
A(S) = \int_{x\in S}dA(\mathbf x).
\end {align}$$   

#### **Measures and Averages**

$$\begin{align}
average(f) = \frac{\int_{x \in S}f(\mathbf x)\,d\mu(\mathbf x)}{\int_{x \in S}d\mu(\mathbf x)}.
\end {align}$$   

### Continuous Probability

#### **One-Dimensional Continuous Probability Density Functions**
Loosely speaking, a *continuous random variable* $x$ is a scalar or vector quantity that “randomly” takes on some value from the real line $R = (−\infty, +\infty)$. The behavior of $x$ is entirely described by the distribution of values it takes. This distribution of values can be quantitatively described by the *probability density function (pdf)*, $p$, associated with $x$ (the relationship is denoted $x \sim p$). The probability that $x$ assumes a particular value in some interval   
$[a, b]$ is given by the following integral:   

$$\begin{align}
Probability(x \in [a, b]) = \int_a^b p(x)\,dx.
\end {align}$$   

The probability distribution function has two characteristics,   

$$\begin{align}
p(x) \geq 0\quad \text{(probability is non-negative)}, \\
\int_{-\infty}^{+\infty}p(x)\,dx = 1 \quad (Probability(x \in \mathbb R) = 1).
\end {align}$$   

#### **One-Dimensional Expected Value**

The average value that a real function $f$ of a one-dimensional random variable with underlying pdf $p$ will take on is called its expected value, $E(f(x))$ (sometimes written $Ef(x)$):   

$$\begin{align}
E(f(x)) = \int f(x)p(x)dx. \\
E(x+y) = E(x) + E(y) \\
\text{also,} \\
E(f(x) + g(y)) = E(f(x)) + E(g(y)).
\end {align}$$ 

#### **Multi-Dimensional Random Variables**

The discussion of random variables and their expected values extends naturally to multi-dimensional spaces. Most graphics problems will be in such higher dimensional spaces. For example, many lighting problems are phrased on the surface of the hemisphere. Fortunately, if we define a measure $\mu$ on the space the random variables occupy, everything is very similar to the one-dimensional case.   

#### **Variance**
The variance, $V (x)$, of a one-dimensional random variable is, by definition, the expected value of the square of the difference between $x$ and $E(x)$:   
$$\begin{align}
V(x) \equiv E([x - E(x)]^2) .
\end {align}$$   

Some algebraic manipulation gives the non-obvious expression:   
$$\begin{align}
V(x) = E(x^2) - [E(x)]^2 .
\end {align}$$   

#### **Estimated Means**
Many problems involve sums of independent random variables $x_i$, where the variables share a common density $p$. Such variables are said to be *independent identically distributed* (iid) random variables. When the sum is divided by the number of variables, we get an estimate of $E(x)$:   

$$\begin{align}
& E(x) \approx \frac{1}{N}\sum_{i=1}^{N}x_i, \\
& Probability\left[E(x) = \lim_{N\to\infty}\sum_{i=1}^{N}x_i \right] = 1.
\end {align}$$   

### Monte Carlo Integration

In this section, the basic Monte Carlo solution methods for definite integrals are outlined. These techniques are then straightforwardly applied to certain integral problems. All of the basic material of this section is also covered in several of the classic Monte Carlo texts.

$$\begin{align}
E(f(x)) = \int_{x\in S}f(x)p(x)d\mu \approx \frac1N\sum_{i=1}^{N}x_i, 
\end {align}$$   

#### **Quasi–Monte Carlo Integration**

A popular method for quadrature is to replace the random points in Monte Carlo integration with *quasi-random points*. Such points are deterministic, but are in some sense uniform.   

Quasi-random points can improve performance in many integration applications. Sometimes care must be taken to make sure that they do not introduce aliasing. It is especially nice that, in any application where calls are made to random or stratified points in $[0, 1]^d$, one can substitute $d$-dimensional quasi-random points with no other changes.   

### Choosing Random Points

We often want to generate sets of random or pseudorandom points on the unit square for applications such as distribution ray tracing. There are several methods for doing this, e.g., jittering (see Section 13.4). These methods give us a set of $N$ reasonably equi-distributed points on the unit square $[0, 1]^2 : (u_1, v_1)$ through $(u_N, v_N)$.   

Sometimes, our sampling space may not be square (e.g., a circular lens), or may not be uniform (e.g, a filter function centered on a pixel). It would be nice if we could write a mathematical transformation that would take our equidistributed points $(u_i, v_i)$ as input and output a set of points in our desired sampling space with our desired density. For example, to sample a camera lens, the transformation would take $(u_i, v_i)$ and output $(r_i, \phi_i)$ such that the new points are approximately equidistributed on the disk of the lens. While we might be tempted to use the transform   

$$\begin{align}
\varphi_i &= 2\pi\,u_i, \\
r_i &= v_iR,
\end {align}$$   

it has a serious problem. While the points do cover the lens, they do so nonuniformly (Figure 14.6). What we need in this case is a transformation that takes equal-area regions to equal-area regions—one that takes uniform sampling distributions on the square to uniform distributions on the new domain.    
There are several ways to generate such non-uniform points or uniform points on non-rectangular domains, and the following sections review the three most often used: function inversion, rejection, and Metropolis.   

![alt](/images/fundcg/14_sample1.png)    

#### **Function Inversion**
![alt](/images/fundcg/14_sample2.png)    

#### **Rejection**
A *rejection* method chooses points according to some simple distribution and rejects some of them that are in a more complex distribution.   

#### **Metropolis**
The *Metropolis* method uses random *mutations* to produce a set of samples with a desired density. This concept is used extensively in the *Metropolis Light Transport algorithm* referenced in the chapter notes. Suppose we have a random point $x_0$ in a domain $S$. Further, suppose for any point $x$, we have a way to generate random $y \sim p_x$. We use the marginal notation $p_x(y) \equiv p(x \to y)$ to denote this density function. Now, suppose we let $x_1$ be a random point in $S$ selected with underlying density $p(x_0 \to x_1)$. We generate $x_2$ with density $p(x_1 \to x_0)$ and so on. In the limit, where we generate an infinite number of samples, it can be proved that the samples will have some underlying density determined by $p$ regardless of the initial point $x_0$.   
















