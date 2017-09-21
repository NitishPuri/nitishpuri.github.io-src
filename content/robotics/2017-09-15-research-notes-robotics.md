---
title: Mobile Robots
author: Nitish
use_math: true
tags: notes, robotics
category: robotics
summary: Minimal notes on some papers or articles that I recently read. Mainly for logging.
series: Robotics
---

Very minimal notes on some papers or articles that I recently read. Mainly for logging purposes.

## **Robotics**

### **ROS**

#### ***tf*: The Transform Library**   
*Tully Foote*   
*Open Source Robotics Foundation*   

* The need for *tf* : to provide a standard way to keep track of coordinate frames and transform data within the entire system to a component user without requiring knowledge of all the coordinate frames.
* *Broadcaster* and *Listner* modules. 
* Closely related to *scene graphs*.   
![alt](/images/papers/tf1.jpg)   
* There are several different sources of information regarding various coordinate frames in a system, coming from sensors connected to hardware. This data can come at different frequencies.
* *tf* must accept asynchronous inputs and be robust to delayed or lost information.
* Must be robust to a distributed computing environment with unreliable networking and non negligible latency.
* Ability to dynamically change the relationship between frames to account for dynamic/varying structure.
* **Design**
* Transforms and frames are represented as a graph with transforms as edges and frames as nodes.
* The graphs can be disconnected, and must be directed ,acyclic and quickly searchable.
* Limiting the graphs to trees enables this.
* Difference from scene graphs: they are made to be iterated across periodically, while *tf* is designed to be queried for values asynchronously.
* History is also required.
* This data collectively is called a *Stamp*.
* *Broadcaster* broadcasts messages every time an update is heard about a specific transform.
* *Listner* collects the values and interpolates using SLERP, without assuming the presence of a future frame.
* The interpolation is a critical ability, as it allows the system to be asynchronous and robust to lost packets.
* *Transform Computation* using chaining. $T_c^a=T_a^b\timesT_b^c$.
* **Strengths :** *Efficiency, Flexibility*
* **Extensions :**
* Support for velocity.
* Transforming data in time.




### **Robot Grasping**

#### **Robotic Grasping and Contact: A Review**   
[*Source*](https://pdfs.semanticscholar.org/54f8/8557554d9a4e517f301cb170bd50cbe4cfc9.pdf)   

* Survey of work done in last two decades.
* Functions of Human hand 
    * Explore : *haptics*
    * Restrain : *fixturing*
    * Manipulation : *dexterous manipulation*
* Closure properties of grasps
    * Contact modelling the grap
* Force Analysis
* Contact model
    * Kinematics of contact
    * Contact compliance
* Measures of grasp performance
* Grasping and the kinematics of the hand
* Dynamics

### **Mobile Robots**
#### **Modular and Reconfigurable Mobile Robots**   
[*Source*](http://128.173.188.245/publications/J13_Modular_Robots_JRAS.pdf)   

* Classification
    * ![alt](/images/papers/modularBots1.jpg)
* Modular robots with mobile configuration change(MCC)
    * S-bots
        * ![alt](/images/papers/modularBots2.jpg)
    * Uni-Rovers
        * ![alt](/images/papers/modularBots3.jpg)
    * JL-I and JL-II
        * ![alt](/images/papers/modularBots4.jpg)
    * Millibots
        * ![alt](/images/papers/modularBots5.jpg)
    * AMOEBA
        * ![alt](/images/papers/modularBots6.jpg)
* Modular robots with whole body locomotion(WBL)
    * Whole body locomotion in chain architecture
        * CONRO/PolyBot
            * ![alt](/images/papers/modularBots7.jpg)
        * GZ-I
        * CKBot
            * ![alt](/images/papers/modularBots8.jpg)
    * Whole body locomotion in a lattice architecture
        * Macro robots in a lattice architecture
            * *Crystalline*
                * ![alt](/images/papers/modularBots9.jpg)
            * *Odin*      
                * ![alt](/images/papers/modularBots10.jpg)
            * *I-Cubes*
                * ![alt](/images/papers/modularBots11.jpg)
            * *Catoms*
                * ![alt](/images/papers/modularBots12.jpg)
        * Mini robots in a lattice archtecture
            * ![alt](/images/papers/modularBots13.jpg)
        * Reconfigurable mechanisms in a lattice architecture
            * ![alt](/images/papers/modularBots14.jpg)
        * Whole body locomotion in a hybrid architecture
            * M-TRAN/iMobot
                * ![alt](/images/papers/modularBots15.jpg)
            * Molecubes
            * ATRON
                * ![alt](/images/papers/modularBots16.jpg)
            * YaMOR
            * SuperBot
                * ![alt](/images/papers/modularBots17.jpg)


