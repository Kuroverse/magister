# This code was intended to run once (and only once) so I made no effort 
# to make it pretty
# Huge thanks to everymac for all the information

import urllib
import urllib2
from BeautifulSoup import BeautifulSoup
import re, htmlentitydefs
import urlparse
import os
import pprint
import json
import HTMLParser

def slugify(string):
    string = re.sub('\s+', '-', string)
    string = re.sub('[\._]', '-', string)
    string = re.sub('[^\w.-]', '', string)
    return string.strip('_.- ').lower()
    
def unescape(text):
    def fixup(m):
        text = m.group(0)
        if text[:2] ==