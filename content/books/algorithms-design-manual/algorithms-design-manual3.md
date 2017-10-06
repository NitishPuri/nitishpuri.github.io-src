---
title: The Algorithms Design Manual, Numerical Problems
tags: algorithms, programming, book, notes
use_math: true
summary: How to design algorithms???
series: The Algorithms Design Manual
date: 2017-10-03
---

## Numerical Problems

*Check out [Numerical Recipes](http://numerical.recipes/)*

Whats different?   

* Issues of Precision and Error. Floating point issues. Use both single and double precision, and think hard when they diverge.
* Extensive Libraries of Code. There is no reason to not to use all thats already written.


### Solving Linear Equations
![alt](/images/algdm/13_linear1.png)   

**Input description:** An $m \times n$ matrix $A$ and an $m \times 1$ vector $b$, together representing $m$ linear equations on $n$ variables.   
**Problem description:** What is the vector $x$ such that $A \cdot  x = b$?



