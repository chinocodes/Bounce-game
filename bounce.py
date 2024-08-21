from tkinter import *
import random
import time

from IPython.terminal.pt_inputhooks import tk

root = Tk()
root.title('Bounce')
root.resizable(0,0)
root.wm_attributes('-topmost', 1)
canvas = Canvas(root, width=500, height=500, bd = 0, highlightthickness=0)
canvas.pack()
root.update()
class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,245,100)
        start = [-3,-2,-7,0,1,2,3]
        random.shuffle(start)
        self.x = start[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hitBottom = False
        self.textPop = False
        self.count = 0


    def hitPaddle(self,pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                self.count += 1
                return True
            return False


    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id) # typ int list
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hitBottom = True
            self.textPop = True
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3
        if self.hitPaddle(pos) == True:
            self.y = -3




class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id,200,300)
        self.x = 0
        self.y = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all("<KeyPress-Left>", self.turn_left)
        self.canvas.bind_all("<KeyPress-Right>", self.turn_right)

    def draw(self):
        self.canvas.move(self.id,self.x,0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        if pos[2] >= self.canvas_width:
            self.x = 0


    def turn_right(self,evt):
        self.x = 3

    def turn_left(self,evt):
        self.x = -3


paddle = Paddle(canvas, "green")
ball = Ball(canvas, paddle,"red")







while 1:
    if ball.hitBottom == False:
        ball.draw()
        paddle.draw()


    if ball.textPop == True:
        canvas.create_text(250, 250, fill="red", text="GAME OVER", font=("Times", 30))
        canvas.create_text(250, 250, fill="red", text="\n \n \n \n \n \nSCORE: "+str(ball.count), font=("Times", 30))
    root.update_idletasks()
    root.update()
    time.sleep(0.01)







root.mainloop()