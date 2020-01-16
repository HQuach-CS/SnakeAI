import numpy as np
from tkinter import *
import random 
import time 

####### Globals #######
BOARD_WIDTH = 400
BOARD_HEIGHT = 400
ROW = 20
COL = 20
WIDTH = 10
DELAY = 100 #(ms)
MOVE = ['l','u','r','d']
#######################

class Node:
    def __init__(self,x,y,canvas,food=None):
        self.x = x
        self.y = y 
        self.isFood = food
        if self.isFood != None:
            self.color = "red"
        else:
            self.color = "green"
        self.rect = canvas.create_rectangle(self.x * WIDTH + 5,self.y * WIDTH + 5,self.x * WIDTH + 15,self.y * WIDTH + 15,outline="black",fill=self.color)

    def move(self,x,y,canvas):
        canvas.delete(self.rect)
        self.x = x 
        self.y = y
        self.rect = canvas.create_rectangle(self.x * WIDTH + 5,self.y * WIDTH + 5,self.x * WIDTH + 15,self.y * WIDTH + 15,outline="black",fill=self.color)

    def copy(self,n,destroy=None):
        self.x = n.x
        self.y = n.y
        self.rect = n.rect
        if destroy != None:
            destroy.delete(n.rect)
        
    def delete(self,canvas):
        canvas.delete(self.rect)

    def check(self,n):
        if self.x == n.x and self.y == n.y:
            return True 
        else:
            return False

class Board(Canvas):
    def __init__(self):
        super().__init__(width=BOARD_WIDTH, height=BOARD_HEIGHT)
        self.draw_board()
        self.pack()
        self.init()

    def init(self):
        self.isAlive = True
        self.head = Node(random.randint(0,COL-1),random.randint(0,ROW-1),self)
        self.food = Node(random.randint(0,COL-1),random.randint(0,ROW-1),self,1)
        self.snake = [] 
        self.score = 0
        print("Running...")
        self.Update()

    def draw_board(self):
        self.grid = []
        for i in range(0,ROW):
            temp = []
            for j in range(0,COL):
                rect = self.create_rectangle(i*WIDTH+5, j*WIDTH+5, i*WIDTH+15, j*WIDTH+15,outline="black", fill="white")
                self.tag_lower(rect)
                temp.append(rect)
            self.grid.append(temp)

    def snake_move(self,d):
        if d == 'l':
            x = -1 
            y = 0
        elif d == 'u':
            x = 0
            y = -1
        elif d == 'r':
            x = 1
            y = 0
        elif d == 'd':
            x = 0 
            y = 1
        else:
            x = 0
            y = 0

        if len(self.snake) > 1:
            for i in range(len(self.snake)-1,0,-1):
                self.snake[i].move(self.snake[i-1].x,self.snake[i-1].y,self)
        if len(self.snake) >= 1:
            self.snake[0].move(self.head.x,self.head.y,self)
        self.head.move(self.head.x+x,self.head.y+y,self)
            

    def add_snake(self):
        self.snake.append(Node(self.head.x,self.head.y,self))

    def checkCollision(self):
        if self.head.x < 0 or self.head.y < 0 or self.head.x >= COL or self.head.y >= ROW:
            self.isAlive = False
            return
        for n in self.snake:
            if self.head.check(n):
                self.isAlive = False 
                return 
        if self.head.check(self.food):
            self.score = self.score + 1
            self.add_snake()
            self.food.move(random.randint(0,COL-1),random.randint(0,ROW-1),self)

    def Update(self):
        self.checkCollision()
        if self.isAlive:
            self.snake_move(random.choice(MOVE))
            self.after(DELAY,self.Update)
        else:
            print("GameOver")
            self.gameOver()

    def gameOver(self):
        for n in self.snake:
            n.delete(self)
        self.head.delete(self)
        self.food.delete(self)
        print("Final Score:",self.score)
        time.sleep(2)
        self.init()

    def left(self,event):
        self.snake_move('l')
    def right(self,event):
        self.snake_move('r')
    def down(self,event):
        self.snake_move('d')
    def up(self,event):
        self.snake_move('u')

class Snake(Frame):
    def __init__(self):
        super().__init__()
        self.board = Board()
        self.pack()

if __name__ == "__main__":
    root = Tk()
    game = Snake()
    root.bind("<Left>",game.board.left)
    root.bind("<Right>",game.board.right)
    root.bind("<Up>",game.board.up)
    root.bind("<Down>",game.board.down)
    root.mainloop()