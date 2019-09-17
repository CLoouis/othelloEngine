from board import *
from evaluation import *
from legal import *
from game import *

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

print("GAME BEGINS! Input your command by using 'row,column' of the grid you want to play")
# For checking purpose only. Delete if the project is finished.
print('arrayLegalMovesO : ',arrayLegalMovesO)
print('arrayLegalMovesX : ',arrayLegalMovesX)
while not gameEnd:
    showBoard(board)
    showScore(board)
    if(playTurn == 'o'):
        if(arrayLegalMovesO):
            print("It's your turn player "+playTurn+", which grid you want to play?")
            koordinat = input("")
            jalan(board, koordinat, playTurn, arrayLegalMovesO, arrayLegalMovesX)
            updateArrayLegalMove(board, arrayLegalMovesO, arrayLegalMovesX)
        else:
            print("Sorry my friend, there is no legal move for you this turn")
    elif(playTurn == 'x'):
        if(arrayLegalMovesX):
            print("It's your turn player "+playTurn+", which grid you want to play?")
            koordinat = input("")
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

showWin()