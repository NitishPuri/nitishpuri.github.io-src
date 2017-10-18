---
title: Soft Robotics
author: Nitish
use_math: true
tags: notes, robotics
category: robotics
summary: Minimal notes on some papers or articles that I recently read. Mainly for logging.
series: Robotics
date: 2017-09-17
---

Very minimal notes on some papers or articles that I recently read. Mainly for logging purposes.

## Soft Robotics

### <a name="soft1"> </a> Soft Robotics: A Perspective—Current Trends and Prospects for the Future
*Carmel Majidi : 2013*   
[*Source*](http://sml.me.cmu.edu/files/papers/majidi_soro2013.pdf)   


* Soft robots are primarily composed of easily deformable matter such as fluids, gels, and elastomers that match the elastic and rheological properties of biological tissue and organs. Like an octopus squeezing through a narrow opening or a caterpillar rolling through uneven terrain, a soft robot must adapt its shape and locomotion strategy for a broad range of tasks, obstacles, and environmental conditions. This emerging class of elastically soft, versatile, and biologically inspired machines represents an exciting and highly interdisciplinary paradigm in engineering that could revolutionize the role of robotics in healthcare, field exploration, and cooperative human assistance.
* Most suitable for environments and applications that require interaction with soft materials and organisms and/or artificial replication of biological functions.   
![alt](/images/papers/soft_1.jpg)   
* Compliance Matching
    * To prevent injury or robot immobility, the surface e of soft robots must be adequately soft and deformable in order to distribute forces over a large contact area and eliminate interfacial stress concentrations.
    * Compliance matching is particularly important in the subdomain of wearable technologies for human motor assistance.
* Potential Applications
    * Soft wearables for human motor assistance.
    * Biologically inspired field robots for autonomous exploration.   
![alt](/images/papers/soft_2.jpg)   
    * At the scales of invertebrates, insects and microorganisms, may also eventually be used for drug delivery, minimally invasive surgery, and medical implants.   
    * It is unlikely that they would be useful for heavy-duty industrial applications.
* Beyond Robotics
    * As the field of soft robotics grows, the supporting softmatter technologies used in sensing, electronics, and actuation will continue to mature and will eventually appear in application domains.
    * Strechable microelectronics.   
![alt](/images/papers/soft_3.jpg)   

## Swarm Intelligence

### <a name="swarm1"> </a> Swarm Intelligence and Its Applications in Swarm Robotics
*ALEKSANDAR JEVTIC, DIEGO ANDINA : Dec 2007*   
[*Source*](http://www.wseas.us/e-library/conferences/2007tenerife/papers/572-074.pdf)    

* An overview of swarm intelligence.   
![alt](/images/papers/swarm1.png)   
* Self-organizing mechanisms
    * Positive feedback
    * Negative feedback
    * Amplification of fluctuations
    * Multiple Interactions
* A *critical* number of individuals are required for *intelligence* to arise.
* **Particle Swarm Optimization**
    * Inspired by the flocking behavior of birds.
    * Composed of *simple* agents moving through multi-dimensional space, governed by a pull towards best known position to it and its neighbors.
* **Ant Colony Optimization**
    * Uses the *trail-laying-trail-following* behavior to communicate.
* Applications os SI,
    * Every problem, application, that in its base has some kind of optimization can be tackled 
    with SI techniques.
* **Swarm Robotics** : Inspired but not limited to SI.
* Criteria
    * *Autonomy* : autonomous units.
    * *Large number* : large homogeneous groups
    * *Limited capabilities* : incapable or inefficient on their own.
    * *Scalability and Robustness* : Loosing some units should not cause a failure.
    * *Distributed coordination* : Local and limited sensing and communication.
* Applications of SR
    * *Foraging* : includes collective exploration, path finding, efficient task allocation and collective transport. Examples, Search-and-rescue and terrain sample collection.
    * *Dangerous tasks* : Ex. demining.
    * *Exploration and mapping* : Collective exploration in space, extra-terrestrial planets and human veins and arteries. 

## Cloud Robotics

### <a name="cloud1"> </a> A Survey of Research on Cloud Robotics and Automation
*Ben Kehoe, Sachin Patil*   
[*Source*](https://people.eecs.berkeley.edu/~pabbeel/papers/2015-TASE-cloud-robotics-survey.pdf)   

* Cloud is defined as, *a model for enabling ubiquitous, convenient, on demand network access to a shared pool of configurable resources (e.g., servers, storage, networks, applications, and services that can be rapidly provisioned and released with minimal management effort or service provider interaction”*   
* And, cloud robot and autonomous systems are defined as, *Any robot or automation system that relies on either data or code from a network to support its operation, i.e., where not all sensing, computation, and memory is integrated into a single standalone system*   
![alt](/images/papers/cloud_1.png)   
* **Big Data**   
![alt](/images/papers/cloud_2.png)   
![alt](/images/papers/cloud_3.png)   
* Includes everything from image data from computer vision tasks to cad data for AR, grasping and pose estimation.
* **Cloud Computing**   
* Includes remote localization and mapping(SLAM), motion planning and more.
![alt](/images/papers/cloud_4.png)   
* **Collective Robot Learning**
* CloudThink, MyRobots and other collective open frameworks.
![alt](/images/papers/cloud_5.png)   
* **OpenSource**
    * ROS, CloudSim OpenRave, Gazebo, Arduino
    * Raven, RoboEarth, RAaaS

## Human Robot Interaction

### <a name="autonomous1"> </a> Robotics and Autonomous Systems
*Thibault Kruse, Amit Kumar Pandey, *
[*Source*](http://www.sciencedirect.com/science/article/pii/S0921889013001048)

* Human-aware navigation is the interaction between research on human-robot interaction and robot motion planning.   
![alt](/images/papers/auto_1.png)   
* Challenges of human-aware navigation
    * Comfort : absence of annoyance and stress for humans in interaction with robots.
        * Eliminate the obvious causes of discomfort.
    * Naturalness : similarities between robots and humans in low-level behavior pattern.
        * Robot motion should be "predictable" by humans.
    * Sociability : adherence to explicit high-level cultural conventions.
        * Social/cultural rules like standing in a queue, and gaze.
        * Context based affordances like not obstructing the view to the TV.
* Towards a human-aware navigation framework
![alt](/images/papers/auto_2.png)   
* *Prediction* based on geometric reasoning or machine learning.(or both)   
![alt](/images/papers/auto_3.png)   
* *Pose Selection* 
* *Path Planning* and human-aware cost functions.
* *Behavior Selection* for interacting with humans.
* *Local Planning* for collision avoidance to ensure the safety of the robot and the environment.
* And the above *feautes* need to be integrated together.

### <a name="uncanny"> </a> The Uncanny Valley
*Masahiro Mori : More than 40 years ago*   
[*Source*](https://spectrum.ieee.org/automaton/robotics/humanoids/the-uncanny-valley)

* How *creepy* are humanoid robots.   
* Most functions are *monotonous*, but this one is not.   
![alt](/images/papers/uncanny_1.png)   
The graph depicts the uncanny valley, the proposed relation between the human likeness of an entity and the perceiver's affinity for it. [*Translators' note: Bunraku is a traditional Japanese form of musical puppet theater dating from the 17th century. The puppets range in size but are typically about a meter in height, dressed in elaborate costumes, and controlled by three puppeteers obscured only by their black robes.*]   
* **The Effect of movement.**   
![alt](/images/papers/uncanny_2.png)   
The presence of movement steepens the slopes of the uncanny valley. The arrow's path in the figure represents the sudden death of a healthy person. [Translators' note: *Noh* is a traditional Japanese form of musical theater dating from the 14th century in which actors commonly wear masks. The *yase otoko* mask bears the face of an emaciated man and represents a ghost from hell. The *okina* mask represents an old man.]   
* Movement can greatly amplify the *creepiness* of a prosthetic hand, or a complete humanoid bot.
* **Escape by design**   
* Design to make them look functional(think about eyeglasses not looking like real eyeballs).
* **An Explanation of the Uncanny**
* No real explanation available, but we still need to map this function accurately so as to build socially acceptable bots.

### <a name="robot-heads"> </a> All  robots are not created equal: The design and perception of humanoid robot heads   
*Carl F. Disalvo et. al*   
[*Source*](https://www.cs.cmu.edu/~kiesler/publications/2002pdfs/2002DiSalvo.robots%20unequal.pdf)   
![alt](/images/papers/heads_1.png)   
* Motivations for design of the (modular)head for *Pearl*. 
![alt](/images/papers/heads_2.png)   
* **Findings** influencing the comparisons
    * The presence of features
    * The dimensions of the head and features and the total number of features
    * Robot heads in comparison to human heads
    * How human-like is *Humanoid*?
* **Design suggestions for a Humanoid Robotic head**
    * *Wide head, wide eyes* : to maintain the robot-ness
    * *Features that dominate the face* : less space for forehead, hair, jaw and chin, to maintain robot-ness.    
    * *Complexity and detail in the eyes* : They express.
    * *Four or more features* : More features provide more human-ness.
    * *Skin* : Depends on the applications, but consumer products must have some kind of skin.
    * *Humanistic form language* : Organic curves and shape to increase the resemblance.

### <a name="social-lstm"> </a> Social LSTM: Human Trajectory Prediction in Crowded Spaces
*Alexandre Alahi et. al*   
[*Source*](https://web.stanford.edu/~alahi/downloads/CVPR16_N_LSTM.pdf)   

* We can *read* other peoples movements, but how can we make the bots do the same.
![alt](/images/papers/slstm_1.png)   
* Previous works try to *model* these interactions, which results in failure in generalization 
for complex crowd activities.
    * **Human-human interactions** : *Social force* model, Gaussian processes and more hand crafted features.
    * **Activity forecasting** : Predict motion in a video, *inverse reinforcement learning*, mostly based on static scene understanding.
    * **RNN models for sequence prediction** 
* **Social LSTM**
* Inspired from *LSTM*s. But they themselves don't have the ability to capture dependencies among multiple correlated sequences.   
![alt](/images/papers/slstm_2.png)   
Overview of our Social-LSTM method. We use a separate LSTM network for each trajectory in a scene. The LSTMs are then connected to each other through a Social pooling (S-pooling)
layer. Unlike the traditional LSTM, this pooling layer allows spatially proximal LSTMs to share information with each other. The variables in the figure are explained later. The bottom row
shows the S-pooling for one person in the scene. The hidden-states of all LSTMs within a certain radius are pooled together and used as an input at the next time-step.
* Each scene is first pre-processed to obtain the spatial coordinates of all the people at different times.
* Introduces social pooling layers for social entities to share information and state.
* The pooling tries to preserve some spatial information through grid based pooling.
* More variations are used, for example only sharing the estimated position(occupancy maps) between neighbors.
* More implementation details in the paper.
* Explains the architecture, different cost functions and comparison with previous state-of-the-art models.

