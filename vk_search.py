#!/usr/bin/python3
# -*- coding: utf-8 -*-


from twi import *
import sys
import codecs
import pprint

#tokens

api_secret = sys.argv[1]

v = vk(api_secret)
ret = (v.search(q = sys.argv[2]))
for strng in ret['response']['items']:
	print (str(strng['text']))
