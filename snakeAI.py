import numpy as np
from tkinter import *
import random 
import time 



class Node:
    def __init__(self,x,y):
        self.x = x # COL
        self.y = y # ROW
    
    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"

    def __eq__(self,other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def change(self,x,y):
        self.x = x
        self.y = y

class Game:
    def __init__(self):
        self.row = 5
        self.col = 5
        self.init()

    def init(self):
        self.grid = np.zeros(shape=(self.row,self.col))
        self.snake = [Node(random.randint(0,self.col-1),random.randint(0,self.row-1))]
        self.food = Node(random.randint(0,self.col-1),random.randint(0,self.row-1))
        self.isAlive = True
        self.score = 0
        self.update_grid()

    def checkCollision(self):
        if self.snake.count(self.snake[0]) > 1 or self.snake[0].x < 0 or self.snake[0].x > (self.col-1) or self.snake[0].y < 0 or self.snake[0].y > (self.row-1):
            self.isAlive = False
        else:
            if self.snake[0] == self.food:
                print("Score++")
                self.score = self.score + 1
                self.food.change(random.randint(0,self.col-1),random.randint(0,self.row-1))
                self.snake.append(Node(self.snake[len(self.snake)-1].x,self.snake[len(self.snake)-1].y))

    def move(self,d):
        for i in range(len(self.snake)-1,0,-1):
            self.snake[i].x = self.snake[i-1].x
            self.snake[i].y = self.snake[i-1].y
        if d == 'l':
            self.snake[0].x = self.snake[0].x - 1
        elif d == 'u':
            self.snake[0].y = self.snake[0].y - 1
        elif d == 'r':
            self.snake[0].x = self.snake[0].x + 1
        elif d == 'd':
            self.snake[0].y = self.snake[0].y + 1
        self.update_grid()
        

    def update_grid(self):
        self.grid = np.zeros(shape=(self.row,self.col))
        for i in self.snake:
            self.grid[i.y][i.x] = 1
        self.grid[self.food.y][self.food.x] = 2
        print(self.grid)

    def play(self):
        MOVE = ['l','r','u','d']
        while True:
            game.move(random.choice(MOVE))
            self.checkCollision()
            if self.isAlive:
                time.sleep(2)
            else:
                print(self.snake[0])
                print("GameOver!")
                print("Score:",self.score)
                break


game = Game()
game.play()
