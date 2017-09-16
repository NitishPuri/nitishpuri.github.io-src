---
title: Research Notes - Robotics
author: Nitish
use_math: true
tags: notes, robotics
category: Summary
summary: Minimal notes on some papers or articles that I recently read. Mainly for logging.
series: Research Notes
---

Very minimal notes on some papers or articles that I recently read. Mainly for logging purposes.

## Robotics

### Robot Grasping

#### Robotic Grasping and Contact: A Review   
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

### Mobile Robots
#### Modular and Reconfigurable Mobile Robots   
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

### Bio Robots

#### OpenRatSLAM : on open source brain-based SLAM system : *Feb 2013*   
[*Source*](http://static.springer.com/sgw/documents/1388513/application/pdf/10-3.pdf)    

* *RatSLAM, OpenRatSLAM, SLAM, Navigation, Mapping, Brain-based, Appearance-based, ROS, Open-source, Hippocampus*
* RatSLAM is a navigation system based on the neural processes underlying navigation in the rodent brain, capable of operating with low resolution monocular image data. This paper describes OpenRatSLAM, an open source version of RatSLAM with bindings to ROS   
* SLAM(Simultaneous Localization and Mapping) , at the core based on SIFT or SURF features.
* This implementation is based on RatSLAM, leveraging tools like OpenCV and ROS. 
* Modular, detailed, integrated with ROS and *rviz*, works online and offline.
* RatSLAM
    * ![alt](/images/papers/ratSlam1.jpg)
    * *Pose Cells, Local View Cells and Experience Map*
* OpenRatSLAM, [code](https://code.google.com/archive/p/ratslam)
    * ![alt](/images/papers/ratSlam2.jpg)
    * Pose Cell Network : represents pose in response to odometric and local view connections. This also makes decisions about the experience map node and link creation.
    * Local View Cells : determines whether a scene is novel or familiar by image comparison techniques. Mostly based on template matching.
    * Experience map : manages graph building, graph relaxation and path planning.
    * Visual Odometry : For image only datasets, provides an odometric estimate based on changes in the visual scene. 
* OpenRatSLAM parameters and tuning
    * ![alt](/images/papers/ratSlam3.jpg) ![alt](/images/papers/ratSlam4.jpg)
    * Iterative tuning by minimizing loss.
* Using OpenRatSLAM
    * Examples of datasets this is used with, and some results.
* Future work
* [Watch In Action](https://www.youtube.com/watch?v=-0XSUi69Yvs)
    
#### Biologically Inspired App*roaches* to Robotics : *March 1997*   
[*Source*](http://pdfs.semanticscholar.org/501b/9eb3c085a66abe4bdd56043fc802c21d0526.pdf)   

* Big gap between fantasy and reality in terms of Autonomous Robots.
* Inspirations from *insects* : agility, adaptability, simplicity
* Focuses on *walking* like an insect.
* From Biology to Robotics
    * Studies done at various levels of integration and inspiration.
* Distributed Gait Control
* A Distributed Neural Network Controller
    * ![alt](/images/papers/bioRobots1.jpg)
* A Stick Insect Controller
    * ![alt](/images/papers/bioRobots2.jpg)
* Evolved Locomotion Controllers
    * Use genetic algorithms to evolve the neural networks for controlling the locomotion.
* Rough Terrain Locomotion

#### The First Takeoff of a Biologically Inspired At-Scale Robotic Insect : *April 2008*   
[*Source*](http://www.micro.seas.harvard.edu/papers/TRO08_Wood.pdf)    

* *Actuators, aerial robotics, biologically inspired robotics, microrobotics*
* Goal is to create an insect-sized, *truly micro* air vehicle.
    * Harvard Microrobotic Fly
    * ![alt](/images/papers/insect1.jpg)
    * Fig. (a) Conceptual drawing highlighting the four primary mechanical and aero-mechanical components.   
    * Fig. (b) First insect-scale flying robot able to takeoff.
* INSECT-FLIGHT
    * Dipteran thoracic mechanics is discussed.
* Creation of a Robotic Insect
    * Actuation
        * Using peizoceramic materials.
    * Transmission
    * Airfoils 
* [Watch In Action](https://www.youtube.com/watch?v=olqaMw8bIb8)

#### Towards Dynamic Trot Gait Locomotion—Design, Control, and Experiments with Cheetah-cub, a Compliant Quadruped Robot : *July 2013*   
[*Source*](https://infoscience.epfl.ch/record/184991/files/Draft1sprowitz2013.pdf)    

* [Watch In Action](https://www.youtube.com/watch?v=_luhn7TLfWU)
* 


