# -*- coding: utf-8 -*-
AUTHOR = u'Abhishek L'
SITENAME = u"Often Bearing Metaphoric Tense"
SITEURL = "0.0.0.0"
TIMEZONE = "Asia/Kolkata"
DEFAULT_DATE_FORMAT = '%d %b %Y'


DISPLAY_PAGES_ON_MENU = True
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'Rants'

PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
LOCALE = ""
DEFAULT_PAGINATION = 4
SUMMARY_MAX_LENGTH = 100
FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
PATH = ('posts')
PAGE_DIR = ('pages')

GITHUB_URL = 'http://github.com/theanalyst/'
DISQUS_SITENAME = "hyperbolicmonologues"
SOCIAL = (('twitter', 'http://twitter.com/abhishekl'),
          ('github', 'http://github.com/theanalyst'),
          ('blogger', 'http://theanalystquotes.blogspot.com')
          )
EMAIL = 'abhishekl.2006@gmail.com'
TWITTER_USERNAME = 'abhishekl'


# global metadata to all the contents
DEFAULT_METADATA = (('yeah', 'it is'),)

# static paths will be copied under the same name
STATIC_PATHS = ["pictures", "images"]
# A list of files to copy from the source to the destination
#FILES_TO_COPY = (('extra/robots.txt', 'robots.txt'),)

COLOPHON = True
COLOPHON_TITLE = 'Colophon'
COLOPHON_CONTENT = \
' Hello there, thanks for the interest to scroll all the way down'\
' This is a blog for random things that I find' \
' interesting. There are two broad categories here, possibly non'   \
' intersecting sections of posts here. Also, Often Bearing Metaphoric' \
' Tense anagrams to the "Importance of Being Earnest", Algernon is unavailable'\
' for comment '
