f = open('e:\\python\\test.txt','r')
line_no=0
count=0
d={}
while True:
    line_no += 1
    line = f.readline()
    if line:
        print(line_no,":",line)
        d[line_no]=len(line.strip())
        if line.strip()[:1]=="P":
            count+=1
    else:
        break
f.close()
print("文件共有%d行"%(line_no-1))
print("以大写字母P开头的有%d行"%count)

max=max(d.values())
min=min(d.values())
for key,value in d.items():
    if value==max:
        print("字符最多的行在%d行，有%d个字符"%(key,value))
    if value==min:
        print("字符最少的行在%d行，有%d个字符"%(key,value))


