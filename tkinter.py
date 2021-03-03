from tkinter import *

def handler1(event):
    print('Hello world!')

def handler2(event):
    exit()
    
#ініціалізація
root = Tk()
hello_label = Label (root, text="Hello, world!!!", font="Times 40")
hello_label.pack()

#привязка обработчиків до пари подія  віджет (подія, обработчик)
hello_label.bind('<Button-1>', handler1)
hello_label.bind('<Button-3>', handler2)

#головний цикл
root.mainloop()
