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

def isGridKosong(baris,kolom):
    global board
    return (board[baris][kolom] == ' ')

def isJalanLegal(giliran,baris,kolom):
    global arrayLegalMovesO,arrayLegalMovesX,playTurn
    tupleKoordinatJalan = (int(baris),int(kolom))
    if(giliran == 'o'):
        return (tupleKoordinatJalan in arrayLegalMovesO)
    elif(giliran == 'x'):
        return (tupleKoordinatJalan in arrayLegalMovesX)
    else:
        return False

def jalan(posisi):
    global board,playTurn
    koordinatJalan = posisi.split(",")
    if(isJalanLegal(playTurn,koordinatJalan[0],koordinatJalan[1])):
        board[int(koordinatJalan[0])][int(koordinatJalan[1])] = playTurn
    # Mengganti giliran jalan
    if(playTurn == 'o'):
        playTurn = 'x'
    elif(playTurn =='x'):
        playTurn = 'o'
    

global arrayLegalMovesO, arrayLegalMovesX,playTurn
arrayLegalMovesO = [(4,2),(5,3),(2,4),(3,5)]
arrayLegalMovesX = [(3,2),(2,3),(5,4),(4,5)]

gameEnd = 0
playTurn = 'o'

# MAIN

print("GAME BEGINS!")
while not gameEnd:
    showBoard(board)
    print("It's your turn player "+playTurn+", which grid you want to play?")
    koordinat = input("")
    jalan(koordinat)
    
