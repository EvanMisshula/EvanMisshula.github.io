#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os

AUTHOR = 'Evan Misshula'
SITENAME = "Evan Misshula"
SITETITLE = "Measure of Justice"
SITESUBTITLE = "Justice, Learning and Probability"
SITEDESCRIPTION = "Evan's encounters with ignorance and injustice"
SITEURL = 'https://evanmisshula.github.io/learning-blog'

SITELOGO = SITEURL + '/images/newProfile200.jpg'  # or .png


PATH = 'content'
TIMEZONE = 'US/Eastern'
DEFAULT_LANG = 'en'
OG_LOCALE = 'en_US'
LOCALE = 'en_US.UTF-8'
I18N_TEMPLATES_LANG = 'en'

# ✅ Use Flex theme
## THEME = os.path.join(os.getcwd(), 'pelican-themes', 'Flex')
THEME = '/home/evan/Documents/columbia/optimalTransport/oldw/ppsite/pelican-themes/Flex'


# ✅ Optional CSS
CUSTOM_CSS = 'static/custom.css'

# ✅ Flex-specific options
MAIN_MENU = True
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = [
    ('Bio','/pages/bio.html'),
    ('Academic','/pages/academic.html'),
    ('Contact','/pages/contact.html'),
    ('CSCI-380','/pages/CSCI380-01.html'),
]

# ✅ Static content
STATIC_PATHS = ['kml', 'images', 'js', 'extra']
IGNORE_FILES = ['.#*', '*~']

# ✅ Social + metadata
GITHUB_URL = 'https://github.com/EvanMisshula'
TWITTER_USERNAME = 'EMisshula'
SOCIAL = (
    ('twitter', 'https://twitter.com/emisshula'),
    ('github', 'https://github.com/EvanMisshula'),
    ('linkedin', 'https://www.linkedin.com/in/evan-misshula'),
)

# ✅ Turn off feeds in development
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# ✅ Pagination
DEFAULT_PAGINATION = 10

# ✅ Development tip (comment out when deploying)
# RELATIVE_URLS = True
