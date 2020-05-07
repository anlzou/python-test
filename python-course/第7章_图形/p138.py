from tkinter import *
win = Tk()
win.title("Label")
lab1 = Label(win,text = '你好',anchor = 'nw')
lab1.pack()

lab2 = Label(win,bitmap = 'question')
lab2.pack()

bm = PhotoImage(file = r"C:\\Users\\anlzou\\Desktop\\图片\\微信图片_20181101224528.png")
lab3 = Label(win,image = bm)
lab3.bm = bm
lab3.pack()
win.mainloop()
