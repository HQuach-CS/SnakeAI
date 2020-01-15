import numpy as np
from tkinter import *
import random 
import time 

####### Globals #######
BOARD_WIDTH = 400
BOARD_HEIGHT = 400
WIDTH = 10
DELAY = 100 #(ms)
#######################

class Board(Canvas):
    def __init__(self):
        super().__init__(width=BOARD_WIDTH, height=BOARD_HEIGHT)
        self.pack()

class Snake(Frame):
    def __init__(self):
        super().__init__()
        self.board = Board()
        self.pack()

if __name__ == "__main__":
    root = Tk()
    game = Snake()
    root.mainloop()