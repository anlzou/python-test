import urllib.parse
import urllib.request

data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding = 'utf-8')
print(data)

response = urllib.request.urlopen('http://httpbin.org/post',data = data)
print(response.read())
