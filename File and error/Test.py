# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 13:41:09 2018

@author: Gavin
"""

import urllib2
import json

html = urllib2.urlopen(r'http://api.douban.com/v2/book/isbn/9787218087351')

hjson = json.loads(html.read())

print( hjson ['rating'])
print (hjson['images']['large'])
print( hjson['summary'])