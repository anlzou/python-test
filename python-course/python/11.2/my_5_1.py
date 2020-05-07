def count_key(filename,key):
    f=open(filename,'r').read()
    count=f.count(key)
    print("在文件{0}中关键字{1}出现了{2}次".format(filename,key,count))

count_key("t1.txt","中国")
count_key("e:\python\hello.txt","the")
    
    
