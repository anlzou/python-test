from math import pi
class Circle(object):
    def __init__(self,r):
        self.r = r
    def getC(self):
        c = 2*pi*self.r**2
        return int(c)
    def getS(self):
        s = pi*self.r**2
        return int(s)
#主函数
c1 = Circle(5)
print('周长：',c1.getC(),'  面积：',c1.getS())
c2 = Circle(10)
print('周长：',c2.getC(),'  面积：',c2.getS())
