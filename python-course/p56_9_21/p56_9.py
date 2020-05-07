for x in range(1,101):
    k = x
    i = len(str(k))
    y = str(x*x)
    j = len(y)
    if(j<=1):
        continue
    y = y[j-i:j+1]
    if(x == int(y)):
        print(x)
