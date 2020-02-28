import tkinter
import random
import time
import numpy as np
import math

class NN:
    def __init__(self):
        self.generationCnt = 200
        self.inputNeuronCnt = 8
        self.hiddenLayerCnt = 2
        self.hiddenNeuronCnt = 18
        self.outputNeuronCnt = 4
        self.fitness = []
        self.weights = [
            {
                'weights': [
                    np.random.uniform(size=(self.inputNeuronCnt,self.hiddenNeuronCnt)),
                    #np.random.uniform(size=(self.hiddenNeuronCnt,self.hiddenNeuronCnt)) for _ in range(self.hiddenLayerCnt - 1),
                    np.random.uniform(size=(self.hiddenNeuronCnt,self.hiddenNeuronCnt)),
                    np.random.uniform(size=(self.hiddenNeuronCnt,self.outputNeuronCnt))], 
                'bias':  [
                    np.random.uniform(size=(1,self.hiddenNeuronCnt)),
                    np.random.uniform(size=(1,self.hiddenNeuronCnt)),
                    np.random.uniform(size=(1,self.outputNeuronCnt))]
            } for _ in range(self.generationCnt)]
        print(self.weights[0])
        
    def newGeneration(self):
        fitnessSum = sum(self.fitness)
        self.fitness = [{'fit': x, 'index' : self.fitness.index(x)} for x in self.fitness]
        self.fitness = sorted(self.fitness, key=lambda fit: fit['fit'],reverse=True)
        for _ in range(self.generationCnt/2):
            parent1 = random.randint(0,math.floor(fitnessSum))
            cnt = 0
            for i in range(len(self.fitness)):
                cnt += self.fitness[i]["fit"]
                if parent1 < cnt:
                    parent1 = self.fitness[i]
                    break
            parent2 = random.randint(0,math.floor(fitnessSum))
            cnt = 0
            for i in range(len(self.fitness)):
                cnt += self.fitness[i]["fit"]
                if parent2 < cnt:
                    parent2 = self.fitness[i]
                    break
            child1tmp = self.weights[parent1["index"]]
            child2tmp = self.weights[parent2["index"]]

    def feedforward(self,i,index):
        hl1 = self.sigmoid(np.dot(i,self.weights[index]["weights"][0]) + self.weights[index]["bias"][0])
        hl2 = self.sigmoid(np.dot(hl1,self.weights[index]["weights"][1]) + self.weights[index]["bias"][1])
        ol = self.sigmoid(np.dot(hl2,self.weights[index]["weights"][2]) + self.weights[index]["bias"][2])
        return ol

    def sigmoid(self,x):
        return 1/(1 + np.exp(-x))

    def fitness(self,steps,foods):
        # Each steps 10 points is rewarded, Each food 10,000 pts is rewarded, On death -1000 pts
        # 200 Steps is maximum per food count (if over, snake dies) 
        # Maybe later, add TimeCnt so low steps count + food = higher reward
        fit = ((steps * 10) + (foods * 10000))
        self.fitness.append(fit)
        return
        
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
    def __init__(self,row,col):
        self.row = row 
        self.col = col

    def Move(self,x,y):
        for i in reversed(range(1,len(self.snake))):
            self.snake[i].x = self.snake[i-1].x 
            self.snake[i].y = self.snake[i-1].y
        self.snake[0].x += x 
        self.snake[0].y += y


    def CheckStatus(self):
        if self.snake[0] in self.snake[1:]:
            self.isAlive = 0
            return
        if self.snake[0].x < 0 or self.snake[0].y < 0 or self.snake[0].x >= self.row or self.snake[0].y >= self.col:
            self.isAlive = 0 
            return
        if self.snake[0] == self.food:
            self.score += 1
            self.food = cell(random.randint(0,self.row),random.randint(0,self.col))
        self.steps += 1

    def Init(self):
        self.snake = [cell(random.randint(0,self.row),random.randint(0,self.col))]
        self.food = cell(random.randint(0,self.row),random.randint(0,self.col))
        self.score = 0
        self.steps = 0
        self.isAlive = 1

    def PlaySnake(self):
        self.Init()
        while self.isAlive:
            move = list(np.random.uniform(size=(1,4)))
            m = move.index(max(move))
            if m == 0:
                self.Move(-1,0)
            elif m == 1:
                self.Move(1,0)
            elif m == 2:
                self.Move(0,-1)
            elif m == 3:
                self.Move(0,1)
            self.CheckStatus()
        return self.score, self.steps
    
game = Snake(10,10)
score,steps = game.PlaySnake()
print(score,steps)

#Goals:
# for index in range(self.generationCnt):
#     results = playsnake(index)
#     fitness(results) ## Append results to self.fitness()
# newGeneration()