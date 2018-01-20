---
title: Fundamentals of Computer Graphics, Part 4
author: Peter Shirley
use_math: true
tags: graphics, notes, programming
series: Fundamentals of Computer Graphics
summary: Surface Shading and Texture Mapping
date: 2017-10-20
---

## Chapter 10 : Surface Shading

### Diffuse Shading
Many objects in the world have a surface appearance loosely described as “matte,” indicating that the object is not at all shiny. Examples include paper, unfinished wood, and dry unpolished stones. To a large degree, such objects do not have a color change with a change in viewpoint. For example, if you stare at a particular point on a piece of paper and move while keeping your gaze fixed on that point, the color at that point will stay relatively constant. Such matte objects can be considered as behaving as **Lambertian objects**.   

#### **Lambertian Shading Model**   

![alt](/images/fundcg/10_lamb1.png) ![alt](/images/fundcg/10_lamb2.png)     

$$\begin{align}c = c_rc_l\text{max}(0, \mathbf{n.l})\end{align}$$   

#### **Ambient Shading**   
$$\begin{align}c = c_r (c_a + c_l\text{max}(0, \mathbf{n.l}))\end{align}$$   

#### **Vertex-Based Diffuse Shading**   
If we apply the above equation to an object made up of triangles, it will typically have a faceted appearance. Often, the triangles are an approximation to a smooth surface. To avoid the faceted appearance, we can place surface normal vectors at the vertices of the triangles (Phong, 1975), and apply Equation (10.3) at each of the vertices using the normal vectors at the vertices (see Figure 10.4). This will give a color at each triangle vertex, and this color can be interpolated using the barycentric interpolation described in Section 8.1.2.

![alt](/images/fundcg/10_phong1.png)     

One problem with shading at triangle vertices is that we need to get the normals from somewhere. Many models will come with normals supplied. If you tessellate your own smooth model, you can create normals when you create the triangles. If you are presented with a polygonal model that does not have normals at vertices and you want to shade it smoothly, you can compute normals by a variety of heuristic methods. The simplest is to just average the normals of the triangles that share each vertex and use this average normal at the vertex. This average normal will not automatically be of unit length, so you should convert it to a unit vector before using it for shading.

### Phong Shading
![alt](/images/fundcg/10_phong2.png)     

Some surfaces are essentially like matte surfaces, but they have **highlights**. Examples of such surfaces include polished tile floors, gloss paint, and whiteboards. Highlights move across a surface as the viewpoint moves. This means that we must add a unit vector e toward the eye into our equations. If you look carefully at highlights, you will see that they are really reflections of the light; sometimes these reflections are blurred. The color of these highlights is the color of the light—the surface color seems to have little effect. This is because the reflection occurs at the object’s surface, and the light that penetrates the surface and picks up the object’s color is scattered diffusely.   

#### **Phong Lighting Model**
We want to add a fuzzy “spot” the same color as the light source in the right place. The center of the dot should be drawn where the direction $e$ to the eye “lines” up with the natural direction of reflection $r$ as shown in Figure 10.5. Here “lines up” is mathematically equivalent to “where $\sigma$ is zero.” We would like to have the highlight have some non-zero area, so that the eye sees some highlight wherever $\sigma$ is small.   

$$\begin{align}c = c_l\text{max}(0, \mathbf{e.r})^p.\end{align}$$   
$p$ is the **Phong Exponent**.   
![alt](/images/fundcg/10_phong3.png)     



$$\begin{align}\mathbf{r} = -\mathbf{l} + 2(\mathbf{l.n})\mathbf{n}\end{align}$$   
![alt](/images/fundcg/10_phong4.png)     


Another heuristic can also be used here,.   
$$\begin{align}\mathbf{h} = \frac{\mathbf{e} + \mathbf{l}}{||\mathbf{e} + \mathbf{l}||}\end{align}$$   
![alt](/images/fundcg/10_phong5.png)     

$$\begin{align}c = c_r (c_a + c_t\text{max}(0, \mathbf{n.l})) +c_lc_p(\mathbf{h.n})^p\end{align}$$   


#### **Surface Normal Vector Interpolation**   
Smooth surfaces with highlights tend to change color quickly compared to Lambertian surfaces with the same geometry. Thus, shading at the normal vectors can generate disturbing artifacts.   

These problems can be reduced by interpolating the normal vectors across the polygon and then applying Phong shading at each pixel. This allows you to get good images without making the size of the triangles extremely small.   

### Artistic Shading
The Lambertian and Phong shading methods are based on heuristics designed to imitate the appearance of objects in the real world.

#### **Line Drawing**
The most obvious thing we see in human drawings that we don’t see in real life is **silhouettes**.   

draw silhouette if $f_0(\mathbf{e})f_1(\mathbf{e}) \leq 0$.   

draw crease if $(\mathbf{n}_0 · \mathbf{n}_1) \leq \text{threshold}$   

#### **Cool-to-Warm Shading**
![alt](/images/fundcg/10_art1.png)     

$$\begin{align}k_w &= \frac{1 + \mathbf{n.l}}{2}.\\
c &= k_wc_w + (1 - k_w)c_c \end{align}$$   

## Chapter 11 : Texture Mapping














