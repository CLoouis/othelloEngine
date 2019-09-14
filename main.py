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

def jalan(posisi):
    global board,playTurn
    koordinatJalan = posisi.split(",")
    board[int(koordinatJalan[0])][int(koordinatJalan[1])] = playTurn
    if(playTurn == 'o'):
        playTurn = 'x'
    elif(playTurn =='x'):
        playTurn = 'o'
    

global arrayLegalMovesO, arrayLegalMovesX,playTurn
arrayLegalMovesO = []
arrayLegalMovesX = []

gameEnd = 0
playTurn = 'o'

# MAIN
print("GAME BEGINS!")
while not gameEnd:
    showBoard(board)
    print("It's your turn player "+playTurn+", which grid you want to play?")
    command = input("")
    jalan(command)
