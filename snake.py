import numpy as np
from tkinter import *
import random 
import time 

####### Globals #######
BOARD_WIDTH = 400
BOARD_HEIGHT = 400
ROW = 10
COL = 10
WIDTH = 10
DELAY = 200 #(ms)
MOVE = ['l','u','r','d']
#######################

class Node:
    def __init__(self,row,col,canvas,food=None):
        self.x = col 
        self.y = row 
        if food == None:
            self.rect = canvas.create_rectangle(self.x * WIDTH + 5,self.y * WIDTH + 5,self.x * WIDTH + 15,self.y * WIDTH + 15,outline="black",fill="green")
        else:
            self.rect = canvas.create_rectangle(self.x * WIDTH + 5,self.y * WIDTH + 5,self.x * WIDTH + 15,self.y * WIDTH + 15,outline="black",fill="red")

    def change(self,n):
        self.x = n.x 
        self.y = n.y 
        self.rect = n.rect

    def move(self,x,y,canvas,food=None):
        self.x = x
        self.y = y
        if food == None:
            self.rect = canvas.create_rectangle(self.x * WIDTH + 5,self.y * WIDTH + 5,self.x * WIDTH + 15,self.y * WIDTH + 15,outline="black",fill="green")
        else:
            canvas.delete(self.rect)
            self.rect = canvas.create_rectangle(self.x * WIDTH + 5,self.y * WIDTH + 5,self.x * WIDTH + 15,self.y * WIDTH + 15,outline="black",fill="red")


class Board(Canvas):
    def __init__(self):
        super().__init__(width=BOARD_WIDTH, height=BOARD_HEIGHT)
        self.init()
        self.pack()

    def init(self):
        self.isAlive = True
        self.snake = [Node(random.randint(0,ROW-1),random.randint(0,COL-1),self)]
        #self.food = Node(random.randint(0,ROW-1),random.randint(0,COL-1),self,1)
        self.food = Node(self.snake[0].y,self.snake[0].x,self,1)
        self.draw_board()
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
        elif d =='d':
            x = 0
            y = 1
        if len(self.snake) > 1:
            self.delete(self.snake[len(self.snake)-1].rect)
            for i in range(len(self.snake)-1,0,-1):
                self.snake[i].change(self.snake[i-1])
        self.snake[0].move(self.snake[0].x+x,self.snake[0].y+y,self)

    def add_snake(self):   
        self.snake.append(Node(self.snake[len(self.snake)-1].y,self.snake[len(self.snake)-1].x,self))

    def checkCollision(self):
        if self.snake[0].x == self.food.x and self.snake[0].y == self.food.y:
            print("Score++")
            self.add_snake()
            self.food.move(random.randint(0,ROW-1),random.randint(0,COL-1),self,1)
            return
        if self.snake[0].x < 0 or self.snake[0].x >= COL or self.snake[0].y < 0 or self.snake[0].y >= ROW:
            self.isAlive = False
            return
        for i in range(1,len(self.snake)):
            if self.snake[0].x == self.snake[i].x and self.snake[0].y == self.snake[i].y:
                self.isAlive = False 
                return

    def Update(self):
        self.checkCollision()
        if self.isAlive:
            print("Running...")
            self.snake_move(random.choice(MOVE))
            self.after(DELAY,self.Update)
        else:
            print("GameOver")
            self.gameOver()
    
    def gameOver(self):
        pass 

class Snake(Frame):
    def __init__(self):
        super().__init__()
        self.board = Board()
        self.pack()



if __name__ == "__main__":
    root = Tk()
    game = Snake()
    root.mainloop()