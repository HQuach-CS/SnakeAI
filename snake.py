import numpy as np
import tkinter as tk
import random 

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

    def create_board(self,snake):
        w = tk.Canvas(self.master, width=400, height=400)
        for i in range(0,snake.col):
            for j in range(0,snake.row):
                if {'col':i,'row':j} in snake.snake:
                    w.create_rectangle(i*10+5,j*10+5,i*10+15,j*10+15,fill="green",outline="black")
                elif {'col':i,'row':j} == snake.food:
                    w.create_rectangle(i*10+5,j*10+5,i*10+15,j*10+15,fill="red",outline="black")
                else:
                    w.create_rectangle(i*10+5,j*10+5,i*10+15,j*10+15,outline="black")
        w.pack()

    def update(self,grid,snake):
        pass

class NeuralNetwork:
    def __init__(self):
        pass


class Snake:
    def __init__(self,row,col):
        self.row = row 
        self.col = col
        self.snake = [{'col':random.randint(0,col-1),'row':random.randint(0,row-1)}]
        self.food = {'col':random.randint(0,col-1),'row':random.randint(0,row-1)}
        pass

if __name__ == "__main__":
    snake = Snake(20,20)
    app = Application(master=tk.Tk())
    app.create_board(snake)
    app.mainloop()