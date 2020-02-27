import tkinter
import random
import time
import numpy as np

class NN:
    def __init__(self):
        self.inputlayercnt = 12
        self.hiddenlayercnt =  18
        self.hiddenlayers = 2
        self.outputlayercnt = 4
        self.weights = [np.random.uniform(size=(self.inputlayercnt,self.hiddenlayercnt)),np.random.uniform(size=(self.hiddenlayercnt,self.hiddenlayercnt)),np.random.uniform(size=(self.hiddenlayercnt,self.outputlayercnt))]
        self.bias = [np.random.uniform(size=(1,self.hiddenlayercnt)),np.random.uniform(size=(1,self.hiddenlayercnt)),np.random.uniform(size=(1,self.outputlayercnt))]
    
    def feedforward(self,i):
        hl1 = self.sigmoid(np.dot(i,self.weights[0]) + self.bias[0])
        hl2 = self.sigmoid(np.dot(hl1,self.weights[1]) + self.bias[1])
        ol = self.sigmoid(np.dot(hl2,self.weights[2]) + self.bias[2])
        print(ol)
        return ol

    def sigmoid(self,x):
        return 1/(1 + np.exp(-x))

    def fitness(self,steps,foods):
        # Each steps 10 points is rewarded, Each food 10,000 pts is rewarded, On death -1000 pts
        # 200 Steps is maximum per food count (if over, snake dies) 
        # Maybe later, add TimeCnt so low steps count + food = higher reward
        return ((steps * 10) + (foods * 10000)) - 1000

class cell:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def draw(self,canvas,fill):
        canvas.create_rectangle(self.x * 20+10,self.y * 20+10,self.x * 20+30,self.y * 20+30,fill=fill)

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, cell):
            return (self.x == other.x and self.y == other.y)
        return False

class Snake:
    def __init__(self,row,col,master):
        self.nn = NN()
        self.master = master
        self.row = row 
        self.col = col
        self.Init()
        self.Board()
        self.Begin()

    def Board(self):
        self.canvas = tkinter.Canvas(master,width=420,height=420)
        self.canvas.pack()
        self.Draw()

    def Move(self,x,y):
        if self.CheckStatus(x,y):
            for i in reversed(range(1,len(self.snake))):
                self.snake[i].x = self.snake[i-1].x 
                self.snake[i].y = self.snake[i-1].y
            self.snake[0].x += x 
            self.snake[0].y += y


    def CheckStatus(self,x,y):
        x += self.snake[0].x 
        y += self.snake[0].y
        snakehead = cell(x,y)
        if(snakehead.x < 0 or snakehead.x >= row or snakehead.y < 0 or snakehead.y >= col):
            self.GameOver()
            return 0
        if snakehead in self.snake[1:]:
            self.GameOver()
            return 0
        if snakehead == self.food:
            self.score += 1
            self.snake.append(cell(self.food.x,self.food.y))
            self.food = cell(random.randint(0,9),random.randint(0,9))
        self.steps += 1
        return 1

    def GameOver(self):
        ## Calculate Fitness
        ## Store Data
        print("Game Over!")
        self.Init()
        self.Draw()

    def Init(self):
        self.snake = [cell(random.randint(0,9),random.randint(0,9))]
        self.food = cell(random.randint(0,9),random.randint(0,9))
        self.score = 0
        self.steps = 0

    def Draw(self):
        self.canvas.delete("all")
        for i in range(0,10):
            for j in range(0,10):
                self.canvas.create_rectangle(i * 20+10,j * 20+10,i * 20+30,j * 20+30)
        for s in self.snake:
            s.draw(self.canvas,"green")
        self.food.draw(self.canvas,"red")

    def Begin(self):
        i = np.random.uniform(size=(1,12))
        move = list(self.nn.feedforward(i)[0])
        m = move.index(max(move))
        if m == 0:
            self.Move(-1,0)
        elif m == 1:
            self.Move(1,0)
        elif m == 2:
            self.Move(0,-1)
        elif m == 3:
            self.Move(0,1)
        self.Draw()
        self.master.after(1000,self.Begin)    


if __name__ == "__main__":
    #### Hyperparameters ####
    col = 10
    row = 10
    #########################

    ####    Globals     #####
    move = ['l','r','d','u']
    #########################
    master = tkinter.Tk()
    game = Snake(row,col,master)

    tkinter.mainloop()



    