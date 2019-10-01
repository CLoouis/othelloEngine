from board import *
from evaluation import *
from legal import *
from game import *
from randombot import *
from execute import *
from gui import *
import random

# board = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]

# board[4][4] = 'x'
# board[4][5] = 'o'
# board[5][4] = 'o'
# board[5][5] = 'x'

# global arrayLegalMovesO, arrayLegalMovesX, playTurn, koordinat
# arrayLegalMovesO = [(5,3),(6,4),(3,5),(4,6)]
# arrayLegalMovesX = [(4,3),(3,4),(6,5),(5,6)]
# gameEnd = False
# playTurn = 'o'

# MAIN
def main():
    root = Tk()
    screen = Canvas(root, width=500, height=600, bg="#468A53")
    screen.pack()
    drawGrid(screen)
    
    board = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]

    board[4][4] = 'x'
    board[4][5] = 'o'
    board[5][4] = 'o'
    board[5][5] = 'x'

    arrayLegalMovesX = [(5,3),(6,4),(3,5),(4,6)]
    arrayLegalMovesO = [(4,3),(3,4),(6,5),(5,6)]
    gameEnd = False
    playTurn = 'o'
    print("Siapakah yang akan bermain sebagai hitam?")
    print("[1] Player")
    print("[2] Random Bot")
    print("[3] Minimax Bot")
    playerO = input("> ")
    print("Siapakah yang akan bermain sebagai putih?")
    print("[1] Player")
    print("[2] Random Bot")
    print("[3] Minimax Bot")
    playerX = input("> ")

    depthO = 1
    depthX = 1

    if (playerO == '3'):
        print("Tingkat Kesulitan bot hitam? [1-6, 6 paling sulit]")
        depthO = int(input(""))
    if (playerX == '3'):
        print("Tingkat Kesulitan bot putih? [1-6, 6 paling sulit]")
        depthX = int(input(""))

    print("GAME BEGINS! Input your command by using 'row,column' of the grid you want to play")
    # For checking purpose only. Delete if the project is finished.
    print('arrayLegalMovesO : ',arrayLegalMovesO)
    print('arrayLegalMovesX : ',arrayLegalMovesX)
    showBoard(board)
    drawBoard(board, screen)
    # showScore(board)
    while not gameEnd:
        # showBoard(board)
        # showScore(board)
        if(playTurn == 'o'):
            if(arrayLegalMovesO):
                koordinat = execute(playerO, board, arrayLegalMovesO, 
                            arrayLegalMovesX, playTurn, depthO)
                jalan(board, koordinat, playTurn, arrayLegalMovesO, arrayLegalMovesX)
                updateArrayLegalMove(board, arrayLegalMovesO, arrayLegalMovesX)
            else:
                print("Sorry my friend, there is no legal move for you this turn")
        elif(playTurn == 'x'):
            if(arrayLegalMovesX):
                koordinat = execute(playerX, board, arrayLegalMovesO,
                            arrayLegalMovesX, playTurn, depthX)
                jalan(board, koordinat, playTurn, arrayLegalMovesO, arrayLegalMovesX)
                updateArrayLegalMove(board, arrayLegalMovesO, arrayLegalMovesX)
            else:
                print("Sorry my friend, there is no legal move for you this turn")
        
        
        gameEnd = cekGameEnd(arrayLegalMovesO, arrayLegalMovesX)
        print("eval state " + playTurn + " = " + str(evalState(playTurn, board, arrayLegalMovesO, arrayLegalMovesX)))
        playTurn = switchPlay(playTurn)

        # For checking purpose only. Delete if the project is finished.
        print('arrayLegalMovesO : ',arrayLegalMovesO)
        print('arrayLegalMovesX : ',arrayLegalMovesX)
        showBoard(board)
        # showScore(board)
        root.update()
        drawBoard(board, screen)
        drawScoreBoard(board, screen)


    # showWin()
    root.mainloop()
main()
