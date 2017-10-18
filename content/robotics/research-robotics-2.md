---
title: Mobile Robots
author: Nitish
use_math: true
tags: notes, robotics
category: robotics
summary: Minimal notes on some papers or articles that I recently read. Mainly for logging.
series: Robotics
date: 2017-09-15
---

Very minimal notes on some papers or articles that I recently read. Mainly for logging purposes.

## Kinematics

### <a name="tf"> </a> *tf*: The Transform Library   
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

### <a name="6dof"> </a> Solving Kinematics Problems of a 6-DOF Robot Manipulator
*Computer Science Department, The University of Georgia : 2015*   
[*Source*](https://www.google.com/url?q=https%3A%2F%2Fwww.researchgate.net%2Ffile.PostFileLoader.html%3Fid%3D57cd4b20615e274c742de265%26assetKey%3DAS%253A402906919522304%25401473071903479&sa=D&sntz=1&usg=AFQjCNF8-U-44kQLISfar99yrIFTYElU9w)   


* An analytical approach for solving forward kinematics problem of a serial robot manipulator with six degrees of freedom and a specific combination of joints and links to formulate the position of gripper by a given set of joint angles.   
![alt](/images/papers/kuka_1.jpg)   
* The functional state of each joint related to its successive joint in the design of this robot is as follows:   
$$ R_1 \bot R_2 \parallel R_3 \bot R_4 \bot R_5 \bot R_6 $$   
in which $R$ indicates a revolute joint and the indices describe the position of the joint relative to the base of the robot.   
* Uses D-H parameter convention for assigning coordinate frames.
* D-H parameter analysis for Kuka KR60 can be found [here]({filename}kuka-kinematics.md)


## Robot Grasping

### <a name="grasping1"> </a> Robotic Grasping and Contact: A Review     
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

## Mobile Robots
### <a name="mobile1"> </a> Modular and Reconfigurable Mobile Robots   
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


