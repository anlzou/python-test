import os
list_dirs = os.walk("E:\\")
#print(list(list_dirs))
for folderName,subFolders,fileNames in list_dirs:
    print("当前目录：" +folderName)
    for subFolder in subFolders:
        print(folderName +"的子目录是——" +subFolder)
    for fileName in fileNames:
        print(subFolder +"的文件是——"+fileName)
