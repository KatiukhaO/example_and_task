import tkinter as tk 
from random import randint

width = 300
height = 200

def canvas_click_handler(event):
    print('hello world! x =', event.x, 'y = ', event.y)

def tick():
    global x, y , dx, dy
    
    x += dx
    y += dy
    if x + r > width or x - r <= 0 :
        dx = - dx
    if y + r > height or y - r <= 0 :
        dy = - dy

    canvas.move(ball_id, dx, dy)
    root.after(50, tick)

def main():
    global root, canvas
    global ball_id, x, y, r, dx, dy

    root = tk.Tk()
    root.geometry(str(width)+"x"+str(height))
    canvas = tk.Canvas(root)
    canvas.pack(anchor = "nw", fill = tk.BOTH)
    canvas.bind('<Button-1>', canvas_click_handler)

    r = randint(20,50)
    x = randint(r, width - r)
    y = randint(r, height - r)
    dx, dy = (+3, +1)
    ball_id = canvas.create_oval(x - r, y - r, x + r, y + r, fill = "green")

    tick()
    root.mainloop()
    
if __name__ == '__main__': 
    main()
