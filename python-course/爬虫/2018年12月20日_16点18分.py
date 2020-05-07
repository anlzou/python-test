import urllib.request
response = urllib.request.urlopen('https://www.baidu.com')
print(type(response))
