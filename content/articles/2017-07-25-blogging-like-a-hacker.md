---
layout: post
title: Blogging like a hacker
comments: true 
category: Meta
tags:
    - jekyll
    - blogging
---


So, finally I was able to settle up for a blog after months of procrastination with multiple frameworks and platforms.   
I had earlier tried to use [Tumblr](http://nitishpuri.tumblr.com/). But, I wanted to be able to explore different areas, like sharing my views on technology that I am currently interested in, music that I am currently digging in, some random art that I create and so on. Tumblr turned out to be a great platform for sharing my art, but for the same reasons did not look like a place where I could write about deep neural networks, natural language and computer vision. Though there are some blogs there that do just [that](http://lewisandquark.tumblr.com/).    
Then I tried Wordpress, but was never able to settle down on something satisfying and never actually pushed anything. It just had too much to fiddle with, so many options, so many plugins. :confused:
This was very difficult for someone like me who opens 20 new browser tabs reading a single post and then bookmarks them all for reading later.:innocent:   
Then I spend two weeks doing [Django tutorials](http://www.tangowithdjango.com/). It was an interesting experience as this was my first time dealing with Python and web frameworks as well. but, in the end, I realized that these are just as many knobs, even if I keep the features minimal, it was too much work for me as I did not wanted to spend so much time building web technology(i would rather complete Skyrim). :grin:
Then, after abandoning my quest for several months, I came across this awesome [article](https://emptysqua.re/blog/write-an-excellent-programming-blog/) about writing programming blogs, and how it is important for being a part of the technical community today. And, naturally, I had another 25 tabs open looking for advice on starting a tech blog and most feasible platforms to do so today.
There I found [this](http://bruceeckel.github.io/2014/11/19/using-github-pages/) post. It talks about using [jekyll](https://jekyllrb.com/) with [github pages](https://pages.github.com/) as a blogging platform. Though I already "knew" about it, but I only thought of as a cleaner way of viewing your `README` files written in markdown. As I read through that article, it was clear to me that I would be able to settle in with this. It was simple to setup, free and simple to host, works with markdown which everybody uses, no necessary knobs to fiddle with databases and hosting providers. It was a great resource as it also listed out other links that I could follow to customize as much as I wanted.

So, I opened up another browser window and started searching for some good themes, which brought me back to the themes originally suggested [here](http://bruceeckel.github.io/2014/11/19/using-github-pages/). So, this website was created using the theme [lanyon](https://github.com/poole/lanyon), which derives from [poole](https://github.com/poole/poole). Jekyll, Poole and Lanyon are all characters from [The Strange Case of Dr. Jekyll and Mr. Hyde](http://en.wikipedia.org/wiki/Strange_Case_of_Dr_Jekyll_and_Mr_Hyde).

I started with forking the theme to my repo, following [this](https://www.smashingmagazine.com/2014/08/build-blog-jekyll-github-pages/) article.

However, before actually posting anything I had to setup up a local environment for jekyll also discussed in the article.

### Customizations
* Added support for Disqus comments.
* Added Google Analytics support.
* Changed some icons.
* Added sections for Timeline and resume
* Added sections for Art gallery.
