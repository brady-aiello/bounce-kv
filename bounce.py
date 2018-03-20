from Tkinter import *
import random
import time

# tk = Tk()
# tk.title("BOUNCE,THE BEST GAME EVER!")
# tk.resizable(0, 0)
# tk.wm_attributes("-topmost", 1)
# canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
# canvas.pack()
# tk.update()


class Ball:

    def __init__(self, canvas, color):
        self.canvas = canvas
        #self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        # self.canvas_width = self.canvas.winfo_width()
        # starts = [-3, -2, -1, 1, 2, 3]
        # random.shuffle(starts)
        # self.x = starts[0]
        # self.y = -3
        # self.canvas_height = self.canvas.winfo_height()
        # self.x = 0
        # self.y = -1
        # self.canvas_width = self.canvas.winfo_width()
        # self.hit_bottom = False
        
    def draw(self):
        self.canvas


        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3

ball = Ball(canvas, "red")

while 1:
    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
