from tkinter import *

class Board :
    def __init__(self):
        self.array = []
        for x in range(10):
            self.array.append([])
            for y in range(10):
                self.array[x].append(None)

        self.array[4][4] = "o"
        self.array[4][5] = "x"
        self.array[5][4] = "x"
        self.array[5][5] = "o"
    
def drawGrid(screen):
    for i in range(7):
        lineShift = 50 + 50 * (i+1)

        screen.create_line(50, lineShift, 450, lineShift, fill="#111")

        screen.create_line(lineShift, 50, lineShift, 450, fill="#111")

def createPion(x, y, stamp, screen):
    if stamp == 'o':
        screen.create_oval(54+50*y,54+50*x,96+50*y,96+50*x,tags="tile {0}-{1}".format(x,y),fill="black")
    elif stamp == 'x' :
        screen.create_oval(54+50*y,54+50*x,96+50*y,96+50*x,tags="tile {0}-{1}".format(x,y),fill="white")

def drawBoard(board, screen):
    for i in range(1, 9):
        for j in range(1, 9):
            createPion(i - 1, j - 1, board[i][j], screen)

def drawScoreBoard(board, screen):
    screen.delete("score")

    white = 0
    black = 0

    for i in range(1,9):
        for j in range(1,9):
            if (board[i][j] == 'o'):
                black += 1
            elif (board[i][j] == 'x'):
                white += 1

    screen.create_text(30,550,anchor="w", tags="score",font=("Consolas", 50),fill="white",text= white)
    screen.create_text(400,550,anchor="w", tags="score",font=("Consolas", 50),fill="black",text=black)
