---
title: Fundamentals of Computer Graphics, Part 6
author: Peter Shirley
use_math: true
tags: graphics, notes, programming
series: Fundamentals of Computer Graphics
summary: Data Structures for Graphics
date: 2017-11-20
---

## Chapter 12 : Data Structures for Graphics

### Triangle Meshes

Most real-world models are composed of complexes of triangles with shared vertices. These are usually known as *triangular meshes*, *triangle meshes*, or *triangular irregular networks (TINs)* and handling them efficiently is crucial to the performance of many graphics programs.   
The minimum information required for a triangle mesh is a set of triangles (triples of vertices) and the positions (in 3D space) of their vertices. But many, if not most, programs require the ability to store additional data at the vertices, edges, or faces to support texture mapping, shading, animation, and other operations. Vertex data is the most common: each vertex can have material parameters, texture coordinates, irradiances—any parameters whose values change across the surface. These parameters are then linearly interpolated across each triangle to define a continuous function over the whole surface of the mesh. However, it is also occasionally important to be able to store data per edge or per face.   

#### **Mesh Topology**

* Every edge is shared by exactly two triangles.
* Every vertex has a single, complete loop of triangles around it.

![alt](/images/fundcg/12_mesh1.png)     
![alt](/images/fundcg/12_mesh2.png)     
![alt](/images/fundcg/12_mesh3.png)     

**Indexed Mesh Storage**   
```
Triangle {
     vector3 vertexPosition[3]
}
```
![alt](/images/fundcg/12_mesh4.png)     
