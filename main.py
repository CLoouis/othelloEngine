from board import *
from evaluation import *
from legal import *
from game import *
from randombot import *
from execute import *
import random

board = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]

board[4][4] = 'o'
board[4][5] = 'x'
board[5][4] = 'x'
board[5][5] = 'o'

global arrayLegalMovesO, arrayLegalMovesX, playTurn, koordinat
arrayLegalMovesO = [(5,3),(6,4),(3,5),(4,6)]
arrayLegalMovesX = [(4,3),(3,4),(6,5),(5,6)]
gameEnd = False
playTurn = 'o'

# MAIN
def main():
    board = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]

    board[4][4] = 'o'
    board[4][5] = 'x'
    board[5][4] = 'x'
    board[5][5] = 'o'

    global arrayLegalMovesO, arrayLegalMovesX, playTurn, koordinat
    arrayLegalMovesO = [(5,3),(6,4),(3,5),(4,6)]
    arrayLegalMovesX = [(4,3),(3,4),(6,5),(5,6)]
    gameEnd = False
    # playTurn = 'o'
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

    print("GAME BEGINS! Input your command by using 'row,column' of the grid you want to play")
    # For checking purpose only. Delete if the project is finished.
    print('arrayLegalMovesO : ',arrayLegalMovesO)
    print('arrayLegalMovesX : ',arrayLegalMovesX)
    depth = 1
    showBoard(board)
    showScore(board)
    while not gameEnd:
        # showBoard(board)
        # showScore(board)
        if(playTurn == 'o'):
            if(arrayLegalMovesO):
                koordinat = execute(playerO, board, arrayLegalMovesO, 
                            arrayLegalMovesX, playTurn, depth)
                jalan(board, koordinat, playTurn, arrayLegalMovesO, arrayLegalMovesX)
                updateArrayLegalMove(board, arrayLegalMovesO, arrayLegalMovesX)
            else:
                print("Sorry my friend, there is no legal move for you this turn")
        elif(playTurn == 'x'):
            if(arrayLegalMovesX):
                koordinat = execute(playerX, board, arrayLegalMovesO,
                            arrayLegalMovesX, playTurn, depth)
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
        showScore(board)
    showWin()

main()
