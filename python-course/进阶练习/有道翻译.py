import urllib.request
import urllib.parse
import json

url = 'http://fanyi.youdao.com/translate?\
    smartresult=dict&smartresult=rule&\
    smartresult=ugc&sessionFrom=null'

def translation(words):
    data = {
        'type': "AUTO",
        'i': words,
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "ue": "UTF-8",
        "action": "FY_BY_CLICKBUTTON",
        "typoResult": "true"
    }

    data = urllib.parse.urlencode(data).encode('utf-8')

    req = urllib.request.Request(url,data)
    #访问改变身份，隐藏机器翻译
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140\
    Safari/537.36 Edge/17.17134')
    re = urllib.request.urlopen(req)
    html = re.read().decode('utf-8')

    target = json.loads(html)
    print('翻译：',target['translateResult'][0][0]['tgt'])
    

#测试
if __name__ == '__main__':
    list_word = input('原文：')
    while list_word != '':
        translation(list_word)
        list_word = input('\n原文：')
