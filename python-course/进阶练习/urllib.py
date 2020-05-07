import urllib.request

#下载猫网的图片
def downimg(path,imgname):
    re = urllib.request.urlopen(path)
    cat_img = re.read()
    
    with open(imgname, 'wb') as f:
        f.write(cat_img)

#测试
if __name__ == '__main__':
    downimg('http://placekitten.com/g/500/600','500_600.jpg')
    downimg('http://placekitten.com/g/600/600','600_600.jpg')
    downimg('http://placekitten.com/g/700/600','700_600.jpg')
    print('ok')
