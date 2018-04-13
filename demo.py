# -*- coding: utf-8 -*-
import ssl
import urllib2
 
context = ssl._create_unverified_context()
response = urllib2.urlopen("https://www.80s.tw/", context=context)
print response.read().decode('utf-8').encode('GB18030')