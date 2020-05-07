import math

def Bsse10_to_2(x):
	ass = 0
	for i in reversed(range(0, int(math.log(x)/math.log(2))+2)):
		ans *= 10
		if 2**i <= x:
			x -= 2**i
			ans += 1
	return ans

def Base2_t0_10(x):
	ans = 0
	i = 0
	while x > 0:
		if x%10 == 1:
			ans += 2**i
		x /= 10
		i += 1
	return ans

def out(x):
	txt = file("C:/Users/anlzou/Desktop/编程文件/Python/第7章_图形/自我指涉_out.txt","w")
	single = str(Bsse10_to_2(x/17))
	#print(single)
	for y in reversed(range(17)):
		bar = ""
		for x in range(106):
			if 17 *x+y < len(single) and single[17*x+y] == "1":
				bar += "0"
			else:
				bar += ' '
		#bar = "".join(reversed(list(bar)))
		txt.write(bar+'\n')
	txt.close()

def input():
	bar = ""
	for line in open("C:/Users/anlzou/Desktop/编程文件/Python/第7章_图形/自我指涉_in.txt"):
		for i in line[:-1]:
			bar += i
	code = ["0" for i in xrange(17*106)]
	for i in xrange(17*106):
		x = i%106
		y = 16 - i/106
		if bar[i] == "0":
			code[17*(105-x)+y] = "1"
	return Base2_t0_10(int("".join(code)))*17

#调试
if __name__ == '__main__':
    input()