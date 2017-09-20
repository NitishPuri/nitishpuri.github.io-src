---
title: Research Notes - Machine Learning
author: Nitish
use_math: true
tags: notes, deep-learning
category: Research
summary: Minimal notes on some papers or articles that I recently read. Mainly for logging.
series: Research Notes
---

Very minimal notes on some papers or articles that I recently read. Mainly for logging purposes.

## **Deep Learning**

### **Image Recognition**

#### **Very Deep Convolutional Networks For Large-Scale Image Recognition**   
*Karen Simonyan, Andrew Zisserman : Apr 2015*   
[*Source*](https://arxiv.org/abs/1409.1556)

* Introduces the *VGG network that won ImageNet in 2014*.
* Deeper ConvNets. Takes input as (224 X 224) RGB and mean image subtracted as preprocessing. Two final FC hidden layers, followed by one FC layer with 1000 outputs. Number of total trainable parameters turn out to be 144 million for VGG-19. 
* All the hidden layers use *ReLU* activations.
* Deeper networks with small filters result in more regularization and less parameters.
* Optimise multinomial logistic regression objective using mini-batch gradient descent with momentum.
* At the end introduces ensemble models by averaging softmax predictions from multiple models.

#### **Deep Residual Learning for Image Recognition**   
*Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun : Dec 2015*   
[*Source*](https://arxiv.org/abs/1512.03385)

* Presents residual learning framework to ease the training of networks that are substantially deeper(152 layers!) than those used previously. *How to win ImageNet in 2015.*
* Problem with deeper networks : *Vanishing Gradients* : Addressed by intermediate normalization.
* Problem with deeper networks : *Degradation*, not caused by overfitting..
![alt](/images/papers/resNet1.jpg)
* Introduces residual learning framework by using shortcut connections that can perform identity mapping.
* Using Identity mapping as precondition allows the network to easily learn the identity, if it is a desired mapping. This helps in *simplifying* networks.
* *Plain Network* architecture, mainly based on VGG nets.
* *Residual Network* architecture, insert shortcuts to the plain network.
* The model shows *no optimization difficulty* even with > 1000 layers..!!
* Finally discusses improvements for detection and localization tasks.

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
 

### **Image Segmentation**

#### **Image segmentation review**   
[*Source*](http://blog.qure.ai/notes/semantic-segmentation-deep-learning-review)   

* A review of segmentation at qure.ai  



#### **A Review of Deep Learning Techniques Applied to Semantic Segmentation**   
*Alberto Garcia-Garcia, Sergio Orts-Escolano, Sergiu Oprea, Victor Villena-Martinez, Jose Garcia-Rodriguez : Apr 2017*
[*Source*](https://arxiv.org/abs/1704.06857)   

* *Semantic Segmentation, Deep Learning, Scene Labeling, Object Segmentation*   
* This paper provides a review on deep learning methods for semantic segmentation applied to various  application areas. This also describes the terminology used as well as some background concepts, then some existing models are reviewed(2017). At last a set of promising future works are discussed.
* These techniques are not very mature as of yet, mainly because of a lack of unifying picture.
![Evolution of object recognition](/images/papers/deepSegment1.jpg)
* CNN Architectures : AlexNet, VGG, GoogleNet, ResNet, etc..
* 2D and 3D Datasets : [PascalVOC](http://host.robots.ox.ac.uk/pascal/VOC/voc2012/),  [Microsoft COCO](6. http://mscoco.org/), and more,...   
* Decoder Variants, Integrating Context Knowledge
* Instance Segmentation
* RGB-D Data and 3D Data
* Video Sequences   



#### **DeepLab : Semantic Image Segmentation with Deep Convolution Nets, Atrous Convolution, and Fully Connected CRFs**   
*Liang-Chieh Chen, George Papandreou, Iasonas Kokkinos, Kevin Murphy, Alan L. Yuille : May 2017*   
[*Source*](https://arxiv.org/abs/1606.00915)    

* *Semantic Segmentation, Atrous Convolution, Conditional Random Fields*
* Introduces upsampled filters(Altrous Convolution) as a tool in dense prediction tasks. Allows us to control the resolution at which feature responses are computed and also allows us to effectively enlarge the field of view of filters to incorporate larger context without increasing the number of parameters or the amount of computation.
* ???? // *Read this again..*


#### **U-Net: Convolution Networks for Biomedical Image Segmentation**   
*Olaf Ronneberger, Philipp Fischer, Thomas Brox : May 2015*
[*Source*](https://arxiv.org/abs/1505.04597)   

* Focuses on end-to-end training for segmentation tasks, relying heavily on data augmentation.
    


#### **Fully Convolutional Networks for Semantic Segmentation**   
*Jonathan Long, Evan Shelhamer, Trevor Darrell : Mar 2015*   
[*Source*](https://arxiv.org/abs/1411.4038)   

* One of the first works to use Fully Connected layers to create pixel heatmap as output.
* Introducing Upsampling or Convolution Transpose.



#### **From Image-level to Pixel-level Labeling with Convolutional Networks**   
*Pedro O. Pinheiro, Ronan Collobert : Apr 2015*   
[*Source*](https://arxiv.org/abs/1411.6228)   

* Weakly supervised segmentation.
* Put more weights to pixels with known class labels.
* Uses part of model trained on ImageNet and trains for segmentation on PascalVOC.

