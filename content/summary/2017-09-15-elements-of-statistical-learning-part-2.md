---
title: Elements Of Statistical Learning, Part 2
author: Trevor Hastie, Robert Tibshirani, Jerome Friedman 
category: Summary
tags: data-science, notes
series: Elements Of Statistical Learning
---

## Chapter 7: Model Assessment and Selection
- Introduction
- Bias, Variance and Model Complexity
![alt](/images/esl/7_bias_var.png)
![alt](/images/esl/7_cross_val.png)
- The Bias-Variance Decomposition
![alt](/images/esl/7_bias_var_trade.png)
    - Example : Bias-Variance Tradeoff
- Optimism of the Training Error Rate
- Estimates of In-Sample Prediction Error
- The Effective Number of Parameters
    - Also known as *effective degree of freedom* $= trace(S)$, where $\hat y=Sy$. 
- The Bayesian Approach and BIC
- Minimum Description Length
- Vapnik-Chervonenkis Dimension ☠ 
- Cross-Validation 👍  
    - K-Fold Cross Validation
    - The Wrong and Right Way to Do Cross-validation
    - Does Cross-Validation Really Work?
- Bootstrap Methods
- Conditional or Expected Test Error? ☠ 

