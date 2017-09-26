---
title: The Algorithm Design Manual
author: Steven S. Skiena
tags: algorithms, notes
series: The Algorithm Design Manual
summary: The Algorithm Design Manual, Part 1
use_math: true
---


## **Chapter 1 : Introduction to Algorithm Design**

Algorithms as procedures.   

**Insertion sort**
```C
void insertion_sort(item s[], int n){
    int i,j;   /* counters*/
    for(i=1; i<n; i++){
      j=i;
      while((j>0) && (s[j] < s[j-1]>)){
        swap(&s[j], &s[j-1]);
        j=j-1;
      }
    }
}
```
### **Robot Tour Optimization**

*Problem:* Robot Tour Optimization.   
*Input:* A set $S$ of $n$ points in the plane.   
*Output:* What is the shortest cycle tour that visits each point in the set $S$?   

> *Take-Home Lesson:* There is a fundamental difference between algorithms, which always produce a correct result, and heuristics, which may usually do a good job but without providing any guarantee.

### **Selecting the right jobs**

*Problem:* Movie Scheduling Problem   
*Input:* A set $I$ of $n$ intervals on the line.   
*Output:* What is the largest subset of mutually non-overlapping intervals which can be selected from $I$?   
> *Take-Home Lesson:* Reasonable-looking algorithms can easily be incorrect. Algorithm correctness is a property that must be carefully demonstrated.   

### **Reasoning about Correctness**   

#### *Expressing Algorithms*

> *Take-Home Lesson:* The heart of any algorithm is an idea. If your idea is not clearly revealed when you express an algorithm, then you are using too low-level a notation to describe it.

#### *Problems and Properties*

> *Take-Home Lesson:* An important and honorable technique in algorithm design is to narrow the set of allowable instances until there is a correct and efficient algorithm. For example, we can restrict a graph problem from general graphs down to trees, or a geometric problem from two dimensions down to one.

#### *Demonstrating Incorrectness*

> *Take-Home Lesson:* Searching for counterexamples is the best way to disprove the correctness of a heuristic.

#### *Induction and Recursion*

> *Take-Home Lesson:* Mathematical induction is usually the right way to verify the correctness of a recursive or incremental insertion algorithm.

### **Modeling the Problem**

#### *Combinatorial Objects*

> *Take-Home Lesson:* Modeling your application in terms of well-defined structures and algorithms is the most important single step towards a solution.

### War Story: Psychic Modeling


## Chapter 2 : Algorithm Analysis

### The RAM Model of Computation

> *Take-Home Lesson:* Algorithms can be understood and studied in a language and machine-independent manner.

#### Best, Worst and Average case Complexity

![alt](/images/algdm/2_time.png)   

### The Big Oh Notation

> *Take-Home Lesson:* The Big Oh notation and worst-case analysis are tools that greatly simplify our ability to compare the efficiency of algorithms.

### Growth Rates and Dominance Relations

#### Dominance Relations

$$
n! >> 2^n >> n^3 >> n^2 >> n\log{n} >> n >> \log{n} >> 1
$$

> *Take-Home Lesson:* Although esoteric functions arise in advanced algorithm analysis, a small variety of time complexities suffice and account for most algorithms that are widely used in practice.


