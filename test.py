# -*- coding: utf-8 -*-
import ssl
import urllib2
import re


context = ssl._create_unverified_context()
response = urllib2.urlopen("https://www.80s.tw/", context=context)
html = response.read().decode('utf-8').encode('GB18030')


pattern = re.compile('<li><a href="(.*?)" style="color:#.*?">(.*?)</a></li>', re.S)
result = re.findall(pattern, html)
if result:
    print '本页共有 %d 个热门词' % len(result)
    for r in result:
        print r[0] + ' ' + r[1]