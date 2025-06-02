#!/usr/bin/env python
# -*- coding: utf-8 -*- #


from __future__ import unicode_literals
import os

AUTHOR = u'Evan Misshula'
SITENAME = u"Evan Misshula"

SITEURL = "https://evanmisshula.github.io/learning-blog"
SITETITLE = "Measure of Justice"  # ✅ From Flex
SITESUBTITLE = "Justice, Learning and Probability"  # ✅ From Flex
SITEDESCRIPTION = "Evan's encounters with ignorance and injustice"  #

TIMEZONE = 'US/Eastern'
DEFAULT_LANG = 'en'
OG_LOCALE = 'en_US'
LOCALE = 'en_US.UTF-8'
I18N_TEMPLATES_LANG = 'en'

##THEME = 'pelican-themes/Flex'

THEME = os.path.join(os.getcwd(), 'pelican-themes', 'Flex')
CUSTOM_CSS = "static/custom.css"  # ✅ Optional custom styling
MAIN_MENU = True  # ✅ Enables top nav bar
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = [
    ('Bio','/pages/bio.html'),
    ('Academic','/pages/academic.html'),
    ('Contact','/pages/contact.html'),
    ('CSCI-380','/pages/CSCI380-01.html'),
]

TIMEZONE = 'US/Eastern'
##THEME = 'pelican-themes/Flex'
##THEME = '/home/evan/Documents/columbia/optimalTransport/oldw/ppsite/pelican-themes/Flex'

#PELICAN_THEMES = '/home/evan/pelican-themes/bootstrap'

DEFAULT_LANG = u'en'
PATH = 'content'
STATIC_PATHS = [ 'kml','images', 'js','extra']
IGNORE_FILES = ['.#*', '*~']
GITHUB_URL = 'http://github.com/EvanMisshula/'
DELETE_OUTPUT_DIRECTORY = False
USE_FOLDER_AS_CATEGORY = True

GITHUB_URL = 'https://github.com/EvanMisshula'
TWITTER_USERNAME = 'EMisshula'
SOCIAL = (
    ('twitter', 'https://twitter.com/emisshula'),
    ('github', 'https://github.com/EvanMisshula'),
    ('linkedin', 'https://www.linkedin.com/in/evan-misshula'),
)



# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('juan reyero', 'http://juanreyero.com/about/'),
         ('Sasha Chua','http://sachachua.com/blog/'),
         ('org-mode tutorials', 'http://orgmode.org/worg/org-tutorials/index.html'),
         ('emacsnyc.org','http://emacsnyc.org'),
         ('Bastien Guerry','http://bzg.fr/index.en.html'),
         ('ian barton','http://ianbarton.net/'),
         ('Fernando Perez','http://blog.fperez.org/'),
)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/emisshula'),
         ('github', 'https://github.com/EvanMisshula'),
         ('linkedin','http://www.linkedin.com/pub/evan-misshula/20/5b/810‎'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
