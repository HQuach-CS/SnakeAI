import tkinter
import random

class node:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "[" + str(self.x) + "," + str(self.y) + "]"

    def draw(self,canvas,fill):
        canvas.create_rectangle(self.x * 20+10,self.y * 20+10,self.x * 20+30,self.y * 20+30,fill=fill)


class Snake:
    def __init__(self):
        self.start()

    def move(self,x,y):
        for i in reversed(range(1,len(self.snake))):
            self.snake[i].x = self.snake[i-1].x 
            self.snake[i].y = self.snake[i-1].y
        self.snake[0].x += x 
        self.snake[0].y += y

    def checkstatus(self):
        if(self.snake[0].x < 0 or self.snake[0].x >= 20 or self.snake[0].y < 0 or self.snake[0].y >= 20):
            self.isAlive = 0
            print("Game Over!")
            self.start()
            return
        for i in range(1,len(self.snake)):
            if self.snake[0].x == self.snake[i].x and self.snake[0].y == self.snake[i].y:
                self.isAlive = 0
                print("Game Over!")
                self.start()
                return
        if(self.snake[0].x == self.food.x and self.snake[0].y == self.food.y):
            self.score += 1
            self.snake.append(node(self.food.x,self.food.y))
            self.food = node(random.randint(0,19),random.randint(0,19))


    def start(self):
        self.snake = [node(random.randint(0,19),random.randint(0,19))]
        self.food = node(random.randint(0,19),random.randint(0,19))
        self.isAlive = 1
        self.score = 0

    def draw(self,c):
        c.delete("all")
        for i in range(0,20):
            for j in range(0,20):
                c.create_rectangle(i * 20+10,j * 20+10,i * 20+30,j * 20+30)
        for i in self.snake:
            i.draw(c,"green")
        self.food.draw(c,"red")

    def moveleft(self,event):
        print("left")
        self.move(-1,0)
        self.draw(c)
        self.checkstatus()
    def moveright(self,event):
        print("right")
        self.move(1,0)
        self.draw(c)
        self.checkstatus()
    def moveup(self,event):
        print("up")
        self.move(0,-1)
        self.draw(c)
        self.checkstatus()
    def movedown(self,event):
        print("down")
        self.move(0,1)
        self.draw(c)
        self.checkstatus()

if __name__ == "__main__":
    game = Snake()
    master = tkinter.Tk()
    c = tkinter.Canvas(master,width=420,height=420)
    c.pack()
    game.draw(c)
    master.bind("<Left>",game.moveleft)
    master.bind("<Right>",game.moveright)
    master.bind("<Up>",game.moveup)
    master.bind("<Down>",game.movedown)

    tkinter.mainloop()



    