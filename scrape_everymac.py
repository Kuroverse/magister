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
        if text[:2] == "&#":
            # character reference
            try:
                if text[:3] == "&#x":
                    return unichr(int(text[3:-1], 16))
                else:
                    return unichr(int(text[2:-1]))
            except ValueError:
                pass
        else:
            # named entity
            try:
                text = unichr(htmlentitydefs.name2codepoint[text[1:-1]])
            except KeyError:
                pass
        return text # leave as is
    return re.sub("&#?\w+;", fixup, text)
    
def parse_all_products():
    urls = [
        "http://www.everymac.com/systems/apple/powermac_g3/index-powermac-g3.html",
        "http://www.everymac.com/systems/apple/mac_server_g3/index-mac-server-g3.html",
        "http://www.everymac.com/systems/apple/powerbook_g3/index-powerbook-g3.html",
        "http://www.everymac.com/systems/apple/powermac_g4/index-powermac-g4.html",
        "http://www.everymac.com/systems/apple/mac_server_g4/index-mac-server-g4.html",
        "http://www.everymac.com/systems/apple/powerbook_g4/index-powerbook-g4.html",
        "http://www.everymac.com/systems/apple/powermac_g5/index-powermac-g5.html",
        "http://www.everymac.com/systems/apple/mac_pro/index-macpro.html",
        "http://www.everymac.com/systems/apple/xserve/index-xserve.html",
        "http://www.everymac.com/systems/apple/imac/index-imac.html",
        "http://www.everymac.com/systems/apple/emac/index-emac.html",
        "http://www.everymac.com/systems/apple/mac_mini/index-macmini.html",
        "http://www.everymac.com/systems/apple/ibook/index-ibook.html",
        "http://www.everymac.com/systems/apple/macbook/index-macbook.html",
        "http://www.everymac.com/systems/apple/macbook_pro/index-macbookpro.html",
        "http://www.everymac.com/systems/apple/macbook-air/index-macbook-air.html",
        "http://www.everymac.com/syste