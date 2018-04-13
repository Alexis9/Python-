def saveImg(imageURL, fileName):
    u = urllib.urlopen(imageURL)
    data = u.read()
    f = open(fileName, 'wb')
    f.write(data)
    f.close()
    u.close()
	
def saveImgd(http://www.baidu.com)