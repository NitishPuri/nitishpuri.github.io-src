---
title: Research Notes - Machine Learning
author: Nitish
use_math: true
tags: notes, deep-learning
category: Summary
summary: Minimal notes on some papers or articles that I recently read. Mainly for logging.
series: Research Notes
---

Very minimal notes on some papers or articles that I recently read. Mainly for logging purposes.

## Deep Learning

### Image Segmentation

#### Image segmentation review   
[*Source*](http://blog.qure.ai/notes/semantic-segmentation-deep-learning-review)   

* A review of segmentation at qure.ai

#### A Review of Deep Learning Techniques Applied to Semantic Segmentation : *Apr 2017*   
[*Source*](https://arxiv.org/pdf/1704.06857)   

* *Semantic Segmentation, Deep Learning, Scene Labeling, Object Segmentation*   
* This paper provides a review on deep learning methods for semantic segmentation applied to various  application areas. This also describes the terminology used as well as some background concepts, then some existing models are reviewed(2017). At last a set of promising future works are discussed.
* These techniques are not very mature as of yet, mainly because of a lack of unifying picture.
* ![Evolution of object recognition](images/papers/deepSegment1.jpg)
* CNN Architectures : AlexNet, VGG, GoogleNet, ResNet, etc..
* 2D and 3D Datasets : [PascalVOC](http://host.robots.ox.ac.uk/pascal/VOC/voc2012/),  [Microsoft COCO](6. http://mscoco.org/), and more,...   
* Decoder Variants, Integrating Context Knowledge
* Instance Segmentation
* RGB-D Data and 3D Data
* Video Sequences   

#### DeepLab : Semantic Image Segmentation with Deep Convolution Nets, Atrous Convolution, and Fully Connected CRFs : *May 2017*   
[*Source*](https://arxiv.org/abs/1606.00915)   

* *Semantic Segmentation, Atrous Convolution, Conditional Random Fields*
* Introduces upsampled filters(Altrous Convolution) as a tool in dense prediction tasks. Allows us to control the resolution at which feature responses are computed and also allows us to effectively enlarge the field of view of filters to incorporate larger context without increasing the number of parameters or the amount of computation.
* ???? // *Read this again..*

#### U-Net: Convolution Networks for Biomedical Image Segmentation : *May 2015*   
[*Source*](https://arxiv.org/abs/1505.04597)   

* Focuses on end-to-end training for segmentation tasks, relying heavily on data augmentation.
    
#### Fully Convolutional Networks for Semantic Segmentation : *Mar 2015*   
[*Source*](https://arxiv.org/abs/1411.4038)   

* One of the first works to use Fully Connected layers to create pixel heatmap as output.
* Introducing Upsampling or Convolution Transpose.

#### From Image-level to Pixel-level Labeling with Convolutional Networks : *Apr 2015*   
[*Source*]((https://arxiv.org/abs/1411.6228))   

* Weakly supervised segmentation.
* Put more weights to pixels with known class labels.
* Uses part of model trained on ImageNet and trains for segmentation on PascalVOC.
    


#### To Read   
* https://arxiv.org/abs/1508.06576
* https://arxiv.org/abs/1311.2901
* https://arxiv.org/pdf/1602.03616.pdf
