#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Nitish Puri'
SITENAME = u'nitishpuri.github.io'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = u'English'

GOOGLE_ANALYTICS = 'UA-103032011-1'

DISQUS_SITENAME  = 'nitishpuri'

GITHUB_URL = 'nitishpuri'



# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DELETE_OUTPUT_DIRECTORY = False

# Blogroll
LINKS = (('Facebook', 'https://www.facebook.com/npuri1903'),
         ('Github', 'https://github.com/nitishpuri'),
         ('Linkedin', 'https://www.linkedin.com/in/nitishpuri/'),)

# Social widget
SOCIAL = (('Facebook', 'https://www.facebook.com/npuri1903'),
         ('Github', 'https://github.com/nitishpuri'),
         ('Linkedin', 'https://www.linkedin.com/in/nitishpuri/'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

OUTPUT_RETENTION = [".git"]

USE_FOLDER_AS_CATEGORY = True

# THEME = 'D:/tree/Portfolio/pelican/pelican-themes/pelican-themes/fresh'
THEME = 'theme/fresh'

PLUGIN_PATHS = ['./plugins']
PLUGINS = [ "render_math", "md_metayaml" , "pelican-toc"]
# '' , 'render_math'
from functools import partial
JINJA_FILTERS = {
    'sort_by_article_count': partial(
        sorted,
        key=lambda tags: len(tags[1]),
        reverse=True)} # reversed for descending order



# Theme Variables :: Fresh
GOOGLE_CUSTOM_SEARCH = '011138406956770016801:3ffzupagszg'
HIDE_CATEGORIES_FROM_MENU = True
SHARETHIS_PUB_KEY = '59baff2dc1263e001291a4b3'

MARKDOWN = {
   'EXTENSIONS' : (['toc'])
}

TOC = {
    'TOC_HEADERS' : '^h[1-3]',
    'TOC_RUN' : 'true',
    'TOC_INCLUDE_TITLE' : 'false'
}