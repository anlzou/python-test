#lambda表达式
L = [lambda x:x**2,lambda x:x**3,lambda x:x**4]

for f in L:
    print (f(2))

print (L[0](3))
