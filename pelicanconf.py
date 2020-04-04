#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Eli Yarson Nabhan'
SITENAME = 'Blog do Eli'
SITEURL = ''

PATH = 'content'
USE_FOLDER_AS_CATEGORY = True
TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
 #        ('Python.org', 'http://python.org/'),
  #       ('Jinja2', 'http://jinja.pocoo.org/'),
   #      ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('linkedin', 'https://linkedin.com/in/eliyarson'),
          ('twitter', 'https://twitter.com/eliyarson'),
          ('github','https://github.com/eliyarson'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Tell Pelican to add files from 'extra' to the output dir
STATIC_PATHS = [
  'extra'
]

# Tell Pelican to change the path to 'static/custom.css' in the output dir
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'static/css/custom.css'}
}

DELETE_OUTPUT_DIRECTORY = False