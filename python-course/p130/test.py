from datetime import date,datetime
import math
class A(object):
    def __init__(self,dict):
        self.dict = dict
    def pr(self):
        print(self.dict)
class B(A):
    def __init__(self,dict):
        A.__init__(self,dict)
    def pr1(self):
        print(self.dict)
        
print(math.pi)
print(type(date.today()))
print(type(date.today().year))

str = '12345'
print(str[0:2])
print(int(str[0:2]))

dict1 = {'an':1,'zhu':2}
dict2 = {'no':0}
print(dict2)
a = A(dict1)
b = B(dict1)
b.pr1()
