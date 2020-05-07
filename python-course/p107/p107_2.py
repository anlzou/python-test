test1 = open("C:\\Users\\anlzou\\手工\\python\\peiqi.txt")
fileContent = test1.readlines()
test1.close()
#print(fileContent)
filewrite = open("C:\\Users\\anlzou\\手工\\python\\peiqi.py","w")
for line in fileContent:
    filewrite.write(line)
filewrite.close()
