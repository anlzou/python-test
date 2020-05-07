from tkinter import *
root = Tk()
root.title("文本框")

test1 = ['C','python','php','html','SQL','java']
test2 = ['CSS','JQuery','Bootstrap']

listb1 = Listbox(root)
listb2 = Listbox(root)
button1 = Button(root,text = "确定")

for i in test1:
    listb1.insert(0,i)
for i in test2:
    listb2.insert(0,i)
    
listb1.pack(side = LEFT)
listb2.pack(side = LEFT)
button1.pack(side = LEFT)
root.mainloop()

