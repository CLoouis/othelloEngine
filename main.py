from board import *
from eval import *

# 
def balikPiece(baris,kolom):
    # Untuk membalik piece pada sebuah kotak
    global board
    if board[baris][kolom] == 'o':
        board[baris][kolom] = 'x'
    elif board[baris][kolom] == 'x':
        board[baris][kolom] = 'o'
    else:
        # ERROR
        print("Blok Kosong!!!")

global arrayLegalMovesO, arrayLegalMovesX
arrayLegalMovesO = []
arrayLegalMovesX = []

gameEnd = 0
playTurn = 'o'

# MAIN
print("GAME BEGINS!")
while not gameEnd:
    showBoard(board)
    print("It's your turn player",playTurn)
    command = input("")
