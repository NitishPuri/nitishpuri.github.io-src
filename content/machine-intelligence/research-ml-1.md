---
title: Neural Networks for Computer Vision
author: Nitish
use_math: true
tags: notes, deep-learning
category: machine-intelligence
summary: Minimal notes on some papers or articles that I recently read. Mainly for logging.
series: Deep Learning
date: 2017-09-05
---

Very minimal notes on some papers or articles that I recently read. Mainly for logging purposes.

## **Deep Learning**

### **Image Recognition**

#### **Very Deep Convolutional Networks For Large-Scale Image Recognition**   
*Karen Simonyan, Andrew Zisserman : Apr 2015*   
[*Source*](https://arxiv.org/abs/1409.1556)   
[*Implementation*](https://github.com/KaimingHe/resnet-1k-layers)   

* Introduces the ***VGG network** that won ImageNet in 2014*.
* Deeper ConvNets. Takes input as (224 X 224) RGB and mean image subtracted as preprocessing. Two final FC hidden layers, followed by one FC layer with 1000 outputs. Number of total trainable parameters turn out to be 144 million for VGG-19. 
* All the hidden layers use *ReLU* activations.
* Deeper networks with small filters result in more regularization and less parameters.
* Optimise multinomial logistic regression objective using mini-batch gradient descent with momentum.
* At the end introduces ensemble models by averaging softmax predictions from multiple models.

#### **Going Deeper with Convolutions**   
*Christian Szegedy, Wei Liu, Yangqing Jia, Pierre Sermanet, Scott Reed, Dragomir Anguelov, Dumitru Erhan, Vincent Vanhoucke, Andrew Rabinovich : Sep 2014*   
*Google DeepMind*   
[*Source*](https://arxiv.org/abs/1409.4842)

* Introduces **"Inception"** with improved utilization of computing resources.
* "We need to go deeper" : But *deeper* networks come with a cost of large number of parameters, which makes the model prone to overfitting, and dramatically increased use of computational resources.
* Fundamental idea : sparsely connected architectures, even inside the convolutions.
* However, the computing infrastructure is very inefficient when it comes to numerical calculations on sparse data structures. And non-uniform sparse structures require careful engineering!
* **Architecture**
![alt](/images/papers/inception1.jpg)   
* **GoogLeNet**
* 22 trainable Layers(100 total layers), low memory footprint.
* Auxillary classifiers are used to allow for efficient gradient propagation. These are used only at training time.

#### **Deep Residual Learning for Image Recognition**   
*Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun : Dec 2015*   
*Microsoft Research*   
[*Source*](https://arxiv.org/abs/1512.03385)

* Presents residual learning framework(**ResNet**) to ease the training of networks that are substantially deeper(152 layers!) than those used previously. *How to win ImageNet in 2015.*
* Problem with deeper networks : *Vanishing Gradients* : Addressed by intermediate normalization.
* Problem with deeper networks : *Degradation*, not caused by overfitting..
![alt](/images/papers/resNet1.jpg)
* Introduces residual learning framework by using shortcut connections that can perform identity mapping.
* Using Identity mapping as precondition allows the network to easily learn the identity, if it is a desired mapping. This helps in *simplifying* networks.
* *Plain Network* architecture, mainly based on VGG nets.
* *Residual Network* architecture, insert shortcuts to the plain network.
* The model shows *no optimization difficulty* even with > 1000 layers..!!
* Finally discusses improvements for detection and localization tasks.

#### **Rethinking the Inception Architecture for Computer Vision**   
*Christian Szegedy, Vincent Vanhoucke, Sergey Ioffe, Jonathon Shlens, Zbigniew Wojna : Dec 2015*   
*Google DeepMind*   
[*Source*](https://arxiv.org/abs/1512.00567)   

* Improving upon **Inception** module and GoogLeNet.
* General guiding principles
    * Avoid representational bottlenecks, especially early in the network.
    * Higher dimensional representations are easier to process locally within a network.
    * Spatial aggregation can be done over lower dimensional embeddings without much or any loss in representational power. 
    * Balance the width and depth of the network.
* Factorizing Convolutions with Large Filter Size
    * Factorize into smaller convolutions. 
        * This results in reduced parameter count.
        * Does this replacement result in any loss of expressiveness?        
![alt](/images/papers/reInception1.jpg)
* Spatial Factorization into Asymmetric Convolutions
![alt](/images/papers/reInception2.jpg)
![alt](/images/papers/reInception3.jpg)

#### **Inception-v4, Inception-ResNet and the Impact of Residual Connections on Learning**   
*Christian Szegedy, Sergey Ioffe, Vincent Vanhoucke, Alex Alemi : Aug 2016*   
*Google DeepMind*   
[*Source*](https://arxiv.org/abs/1602.07261)   

* Combining **Residual networks with Inception architecture**.
* Uniform Inception-v4 blocks are introduced for cleaner architecture. 

### **Deep Visualization**

#### **Visualizing and Understanding Convolutional Networks**  
*Matthew D Zeiler, Rob Fergus L : Nov 2013*   
[*Source*](https://arxiv.org/abs/1311.2901)   

* Understanding why CNNs perform well on Image Classification tasks.
* Visualizing with a Deconvnet
![alt](/images/papers/visnet1.jpg)
* Feature Visualization
![alt](/images/papers/visnet2.jpg)
![alt](/images/papers/visnet3.jpg)
![alt](/images/papers/visnet4.jpg)
![alt](/images/papers/visnet5.jpg)
* Feature Evolution during training
![alt](/images/papers/visnet6.jpg)
* Feature Invariance
* Occlusion Sensitivity
![alt](/images/papers/visnet7.jpg)
![alt](/images/papers/visnet8.jpg)
* Correspondence Analysis  


#### **Multifaceted Feature Visualization: Uncovering the Different Types of Features Learned By Each Neuron in Deep Neural Networks**   
*Anh Nguyen, Jason Yosinski, Jeff Clune : May 2016*    
[*Source*](https://arxiv.org/abs/1602.03616)   

* Researchers have been using *activation maximization* techniques until now. This assumes that each neuron detects only one type of feature.
* But, we know neurons can be *multifaceted*. Here *multifaceted feature visualization* (MFV) is introduced.
    * Systematically visualize all facets of a neuron.
    * Improve image quality of synthesized images with natural and globally consistent colors.
![alt](/images/papers/multiVis1.jpg)
* *Center biased regularization* is used so that the synthesized images dont have many repeated object fragments.
    * This is done by first producing a blurry image, then updating the center pixels more than the edge ones, producing a final image that is sharp and has a centrally-located object.
    * This image would have far fewer duplicated fragments.
![alt](/images/papers/multiVis2.jpg)
* Visualizing the multifaceted nature of hidden neurons
![alt](/images/papers/multiVis3.jpg)
![alt](/images/papers/multiVis4.jpg)
* Discusses various optimization techniques to produce better images in detail : center biased regularization, mean image initialization.
 


