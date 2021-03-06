#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'pcc'
SITENAME = '王子総合パソコン部HP'
SITEDESCRIPTION = '王子総合高校パソコン部の非公式ホームページです。お知らせや活動状況を投稿します。'
SITEURL = ''

PATH = 'content'

THEME = './themes/pelican-fh5co-marble'
JINJA_ENVIRONMENT = {
    "extensions": ["jinja2.ext.i18n"]
}
PLUGINS = ["i18n_subsites"]
PLUGIN_PATHS = ['plugins']

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'ja'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

FAVICON = 'images/favicon.png'
LOGO = 'images/logo.svg'

# Blogroll
LINKS = (('School', 'http://www.oji-sogo-h.metro.tokyo.jp/site/zen/'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/ospc956'),
          ('github', 'https://github.com/OSH-PCC'),)

DEFAULT_PAGINATION = 10
DEFAULT_CATEGORY = 'blog'

GOOGLE_SITE_VERIFICATION_TOKEN = 'eb4ctB-VxH3AnUu7O5hJobwLDssB4DfVLB1-0X-dF40'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
