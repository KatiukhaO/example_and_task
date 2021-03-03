import tkinter as tk 
from random import randint

width = 300
height = 200


class Ball:
    def __init__(self):
        self.r = randint(20,50)
        self.x = randint(self.r, width - self.r)
        self.y = randint(self.r, height - self.r)
        self.dx, self.dy = (+3, +1)
        self.ball_id = canvas.create_oval(self.x - self.r, self.y - self.r,
                                          self.x + self.r, self.y + self.r, fill = "green")

    def move (self):
        self.x += self.dx
        self.y += self.dy
        if self.x + self.r > width or self.x - self.r <= 0 :
            self.dx = - self.dx
        if self.y + self.r > height or self.y - self.r <= 0 :
            self.dy = - self.dy

    def show (self):
        canvas.move(self.ball_id, self.dx, self.dy)
        pass


def canvas_click_handler(event):
    print('hello world! x =', event.x, 'y = ', event.y)

def tick():
    for ball in balls:
        ball.move()
        ball.show()
    root.after(50, tick)

def main():
    global root, canvas, balls

    root = tk.Tk()
    root.geometry(str(width)+"x"+str(height))
    canvas = tk.Canvas(root)
    canvas.pack(anchor = "nw", fill = tk.BOTH)
    canvas.bind('<Button-1>', canvas_click_handler)
    balls = []
    for i in range(5):
        balls.append(Ball())
    tick()
    root.mainloop()
    
if __name__ == '__main__': 
    main()
