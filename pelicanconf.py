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

GITHUB_USER = 'nitishpuri'
GITHUB_SKIP_FORK = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

CC_LICENSE = "CC-BY-NC-SA"

DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search')

DELETE_OUTPUT_DIRECTORY = False
OUTPUT_RETENTION = [".git"]

ARTICLE_URL='posts/{category}/{slug}/'
ARTICLE_SAVE_AS='posts/{category}/{slug}/index.html'
PAGE_URL='pages/{slug}/'
PAGE_SAVE_AS='pages/{slug}/index.html'
CATEGORY_URL='category/{slug}/'
CATEGORY_SAVE_AS='category/{slug}/index.html'
TAG_URL='tag/{slug}/'
TAG_SAVE_AS='tag/{slug}/index.html'
ARCHIVES_URL='archives/'
ARCHIVES_SAVE_AS='archives/index.html'


# Don't generat Authors page 
AUTHOR_SAVE_AS=''

# Blogroll
LINKS = ( )

# Social widget
SOCIAL = (('Facebook', 'https://www.facebook.com/npuri1903'),
         ('Github', 'https://github.com/nitishpuri'),
         ('Linkedin', 'https://www.linkedin.com/in/nitishpuri/'),
         ('Instagram', 'https://www.instagram.com/purinitish/'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

USE_FOLDER_AS_CATEGORY = True

THEME = 'D:/tree/Portfolio/pelican/pelican-themes/pelican-bootstrap3'
# THEME = 'theme/fresh'
# THEME = 'theme/photowall'

PLUGIN_PATHS = ['./plugins']
# PLUGIN_PATHS = ['D:/tree/Portfolio/pelican/pelican-plugins']
PLUGINS = [ "render_math", "md_metayaml" , "pelican-toc", "series",
            "photos", "i18n_subsites", "tag_cloud", "tipue_search",
            "liquid_tags.img"]
# '' , 'render_math'

from functools import partial
# from slugify import slugify
from pelican.utils import slugify

# def slugifyName(name):
#     return slugify(name.split('.')[0])

JINJA_FILTERS = {
    'sort_by_article_count': partial(
        sorted,
        key=lambda tags: len(tags[1]),
        reverse=True),
    'slugify' : lambda name : slugify(name.split('.')[0])
        } # reversed for descending order


JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}


# Theme Variables :: Fresh
GOOGLE_CUSTOM_SEARCH = '011138406956770016801:3ffzupagszg'
HIDE_CATEGORIES_FROM_MENU = True
# SHARETHIS_PUB_KEY = '59baff2dc1263e001291a4b3'
ADDTHIS_PROFILE = 'ra-59bc69ad3aa13e47'
ADDTHIS_DATA_TRACK_ADDRESSBAR = False

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_SIDEBAR = True

SHOW_ARTICLE_AUTHOR = True
SHOW_ARTICLE_CATEGORY = True
DISPLAY_SERIES_ON_SIDEBAR = True

BOOTSTRAP_THEME = 'cosmo'
# BOOTSTRAP_FLUID = True

# BOOTSTRAP_NAVBAR_INVERSE = True
# BANNER = 'images/banner.jpg'

# USE_OPEN_GRAPH = True
# OPEN_GRAPH_FB_APP_ID = '202018593182706'
# OPEN_GRAPH_IMAGE = 'images/dandydev.png'
# TWITTER_CARDS = True

# AVATAR = 
# ABOUT_ME = 
# BANNER = '/path/to/banner.png'
# BANNER_SUBTITLE = 'This is my subtitle'

DISPLAY_TAGS_INLINE = True

# Photos plugin
PHOTO_LIBRARY = 'gallery'
PHOTO_GALLERY = (1024, 768, 80)
PHOTO_ARTICLE = (1024, 768, 80)
PHOTO_THUMB = (450, 330, 80)
PHOTO_RESIZE_JOBS = -1  # Async version is not working,.!!
PHOTO_WATERMARK = True
# PHOTO_WATERMARK_TEXT = 'Nitish'
# PHOTO_WATERMARK_IMG = ''
PHOTO_JSON = 'gallery.json'

# OUTPUT_PATH = 

MENUITEMS = [#('Archives', '/archives/'),
             ('Bio', '/pages/bio/'),
             ('Gallery', '/pages/gallery/')]

MARKDOWN = {
   'EXTENSIONS' : (['toc'])
}

TOC = {
    'TOC_HEADERS' : '^h[1-4]',
    'TOC_RUN' : 'true',
    'TOC_INCLUDE_TITLE' : 'false'
}

MATH_JAX = {
    'align' : 'left',
    'linebreak_automatic' : True
}

# LOG_FILTER = []

# Use while developing
# WRITE_SELECTED = ['output/summary/research-notes-machine-learning.html']