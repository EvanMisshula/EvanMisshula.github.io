#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os

AUTHOR = 'Evan Misshula'
SITENAME = "Evan Misshula"
SITETITLE = "Measure of Justice"
SITESUBTITLE = "Probability, Learning and Justice"
SITEDESCRIPTION = "Evan's encounters with ignorance and injustice"
SITEURL = 'https://evanmisshula.github.io/learning-blog'
SITEURL = ''
SITELOGO = SITEURL + '/images/newProfile200.jpg'  # or .png

PATH = 'content'
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'

THEME = os.path.join(os.getcwd(), 'pelican-themes', 'Flex')

# Optional: basic static path config
STATIC_PATHS = ['images']

# Flex theme options
##SITELOGO = SITEURL + '/images/logo.png'  # Make sure the file exists in content/images/
SITELOGO = SITEURL + '/images/newProfile200.jpg'  # or .png

# Basic menu and social (optional)
MAIN_MENU = True
SOCIAL = (('GitHub', 'https://github.com/yourname'),)

# Development convenience
RELATIVE_URLS = True
ARTICLE_EXCLUDES = ['articles/drafts']
PAGE_EXCLUDES = ['pages/drafts']
