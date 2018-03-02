---
title: Game Engine Architecture
author: Jason Gregory
tags: game engine, graphics, architecture
use_math: true
summary: Really short overview of the book.
---

**All the technology that goes in making a AAA game!!!!**

## Foundations

### Introduction
* Industry overview
* Structure of a Typical Game Team 
    * Engineers
    * Artists
    * Game Designers
    * Producers
    * Other Staff 
    * Publishers and Studios
* What is a Game??
    * Video Games as Soft Real-Time Simulations
* What is a Game Engine??
    * Engine Differences across Genres
        * First-Person Shooter(Quake, Unreal Tournament, Half Life)   
        * Platformers and Other Third-Person Games(Gears of War, Dead Space, Red Dead Redemption, Uncharted)
        * Fighting Games(Soul Calliber, Tekken, Fight Night)
        * Racing Games(NFS, Gran Turismo, Mario kart)
        * Real Time Strategy(Warcraft, Starcraft, Command and Conquer, Age of Empires)
        * Massively Multiplayer Online Games(World of Warcraft, Destiny)
        * Player Authored Content(Mods)(Minecraft)
        * Other Games(sports, RPG, puzzle games, social sims, text based!!)
* Game Engine Survey 
    * The Quake Family of engines -- Quake, Sin, Medal of Honour (ID Software)
    * The Unreal Family of Engines -- Unreal Tournament, Gears of War (Epic Games)
    * The Half-Life Source Engine -- Half-Life, Team Fortress, Portal (Valve)
    * DICE's Frostbite -- Battelfield, Mass Effect, Need for Speed, Dragon Age (EA)
    * CryEngine -- Far Cry, Crysis, Warface (Crytek)
    * Son's PhyreEngine -- Demon's Souls, Dark Souls, Darksiders
    * Microsoft XNA Game Studio 
    * Unity 
    * 2D Engines, and others
* Open source and proprietary engines
* Runtime Engine Architecture
    * Target hardware, device drivers, operating system, 
    * middleware and third-party SDKs, 
        * DS and Algo, Graphics, Collision and Physics, Character Animation, Character Models
    * platform independence layer, core systems, resource manager, rendering engine, 
    * front end, profiling and debugging tools, human interface devices, audio, online multiplayer/networking
    * gameplay foundation systems, event subsystem, scripting system, AI foundations, game specific susbsystems
* Tools and asset pipeline
    * Digital content creation tools, Asset conditioning tools, World Editor, Resource database

### Tools of the Trade
* Version Control
* Visual Studio / IDE
* Profiling Tools
* Memory Leak and Corruption Detection

### Fundamentals of Software Engineering for Games
* C++ Review and Best Practices
* Data, Code and Memory
* Caching and Handling errors
* Pipelines, Caches and Optimization
    * Parallelism, memory caches, instruction pipelining and Superscalar CPUs, 

### 3D Math for Games
* Solving 3D Problems in 2D
* Points and Vectors
    * Coordinate spaces, vector operations
* Matrices
    * matrix operations, Homogeneous coordinates, transformations, matrices in memory, 
* Quaternions
    * quaternions operations, rotation, interpolation, 
* Comparison of Rotational Representations
    * Euler angles, matrices, axis + angle, quaternions,
* Other useful Mathematical Objects
    * Lines, Rays and Line Segments
    * Spheres
    * Planes
    * Axis-Aligned Bounding Box(AABB)
    * Frusta
* Hardware Accelerated SIMD Math
    * SSE Registors, intrinsics, vector-matrix multiplication
* Random Number Generation
    * Linear Congruential Generators
    * Mersenne Twister
    * Mother-of-all and XorShift

## Low Level Engine Systems

### Engine Support Systems
* Subsystem Start-Up and Shut-Down
    * Singleton Approaches
    * OGRE example
    * Naughty Dog's *Uncharted/The Last of Us* series.
* Memory Management
    * Issues:
        * Dynamic memory allocation
        * Memory access patterns
    * Custom Allocators
        * Stack based allocators
        * Pool allocators
* Containers
    * Container Operations, Iterators, Algorithmic Complexity
    * Building Custom Container Classes
* Strings
* Engine Configuration
    * Loading and Saving Options and Per-User options
        * Text files, XML, compressed binary, windows registry, command line options
        * environment variables, online user profiles
    * Examples
        * Quake's Cvars
        * OGRE : Windows INI
        * Naughty Dog : In-Game Menu Settings, Command Line Arguments, Scheme Data Definitions

### Resources and the File System
* File System
    * File names and Paths 
        * Across different operating systems, absolute and relative paths, search paths, path APIs
    * Basic File I/O
        * synchronous and asynchronous File I/O
* The Resource Manager
    * Offline Resource Management and the Tool Chain
        * Revision control of assets
        * The Resource database
            * Examples : UnrealEd, Naughty Dog's Builder, OGRE's Resource Management System
        * The Asset Conditioning Pipeline
    * Runtime Resource Management
        * Responsibilities :
            * Maintain a single copy in memory, Manage lifetime, load and unload, composite resources
            * Maintain referential integrity, manage memory usage, custom processing on load
            * Unified interface, Handles streaming
        * Resource File and Directory Organization
        * Composite Resources and Referential Integrity
        * Handling Cross-References between resources.
        * Post-Load Initialization

### The Game Loop and Real-Time Simulation
* The Rendering Loop
```C++
while(!quit) { 
    updateCamera(); 
    updateSceneElements();
    renderScene();
    swapBuffers();
}
```
* The Game Loop
    * Many interacting subsystems.
    * Each subsystem may work at a different refresh rate and synchronize with each other.
    * A Simple Example : *Pong*
```C++
void main() // Pong 
{
    initGame();
    while(true) {   // game loop
        readHumanInterfaceDevices();
        if(quitButtonPressed) {
            break;  // break out of the game loop
        }
        movePaddles();
        moveBall();
        collideAndBounceBall();
        if(ballImpactSide(LEFT_PLAYER)) {
            incrementScore(RIGHT_PLAYER);
            resetBall();
        }
        else if(ballImpactSide(RIGHT_PLAYER)) {
            incrementScore(LEFT_PLAYER);
            resetBall();
        }

        renderPlayField();
    }
}
```
* Game Loop Architectural Styles
    * Windows Message Pumps
    * Callback-Driven Frameworks
```C++      
// The Framework!!
while(true) {
    foreach(frameListener) {
        frameListener.frameStarted();
    }
    renderCurrentScene();
    foreach(frameListener) {
        frameListener.frameEnded();
    }
    finalizeSceneAndSwapBuffers();
}
```
```C++
// A frame listener implementation
class GameFrameListener : public FrameListener 
{
public:
    virtual void frameStarted() {
        // Things that must happen before rendering
        pollInputDevices();
        updatePlayerControls();
        updateDynamics();
        resolveCollisions();
        updateCamera();
        // etc.
    }
    virtual void frameEnded() {
        // Things to do after scene rendering
        drawHud();
        // etc.
    }
}
```
    * Event Based Updating
* Abstract Timelines
    * Real Time
    * Game Time
    * Local and Global Timelines
* Measuring and Dealing with Time
    * Frame Rate and Time Deltas
    * From Frame Rate to Speed
        * Old-School CPU Dependent Games
        * Updating Based on Elapsed Time
        * Using a Running Average
        * Governing the Frame Rate
        * Screen Tearing and V-Sync
    * Measuring Real Time with High-Resolution Timer
        * High Resolution Clock Drift : In multi-processor architecture
    * Time Units and Clock Variables
        * 64-Bit Integer Clocks
        * 32-Bit Integer Clocks
        * 32-Bit Floating-Point Clocks
        * Other Time Units
    * Dealing with Breakpoints
    * A Simple Clock Class
* Multiprocessor Game Loops
    * Multiprocessor Game Loop Architectures
        * Xbox 360, PlayStation 3, PlayStation 4, Xbox One
    * SIMD
    * Fork and Join
    * One Thread per Subsystem
    * Jobs
    * 




