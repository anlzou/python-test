#error

from tkinter import *
def leftCkick(event):
    print(event.x,event.y)
    point = [event.x,event.y]
    return point

win = Tk()
cv = Canvas(win)
win.title("Label")
win.geometry("400x200")


point = cv.bind("<Button-1>",leftCkick)
line1 = cv.create_line((0,0,point[0],point[1]),fill = 'red',width = 2)
cv.pack()
win.mainloop()