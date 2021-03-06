#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'https://yarson.xyz'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

THEME = 'themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'simplex'
PLUGIN_PATHS = ['plugins/']
PLUGINS = ['i18n_subsites','pelican_gist']
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n']
}

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
DELETE_OUTPUT_DIRECTORY = False

