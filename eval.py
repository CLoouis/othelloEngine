from board import *
from main import arrayLegalMovesO, arrayLegalMovesX

def evalCoinParityEvaluation(playTurn, board):
    """Menghitung perbandingan banyaknya piece milik sendiri 
    dibanding dengan milik musuh"""

    numberOfPlayTurnPiece = 0
    numberOfEnemiesPiece = 0

    for i in range(1, 9):
        for j in range(1, 9):
            if (board[i][j] == playTurn):
                numberOfPlayTurnPiece += 1
            elif (board[i][j] != ' ') :
                numberOfEnemiesPiece += 1
    
    return numberOfPlayTurnPiece - numberOfEnemiesPiece


def mobilityEvaluation(playTurn, board, arrayLegalMovesO, arrayLegalMovesX):
    """Menghitung perbandingan banyaknya kemungkinan jalan dari turn pemain
    saat ini dan turn pemain berikutnya"""

    if (playTurn == 'o'):
        return arrayLegalMovesO - arrayLegalMovesX
    else :
        return arrayLegalMovesX - arrayLegalMovesO

# def stabilityEvaluation():


# board[1][1] = 'x'
# showBoard(board)
# print(evalCoinParityEvaluation('o', board))
