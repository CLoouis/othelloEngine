from board import *
from eval import *

global arrayLegalMovesO, arrayLegalMovesX,playTurn,koordinat

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

def removeKoordinatDariArrayLegal(giliran,baris,kolom):
    global arrayLegalMovesO,arrayLegalMovesX,playTurn
    tupleKoordinatJalan = (int(baris),int(kolom))
    if(giliran == 'o'):
        arrayLegalMovesO.remove(tupleKoordinatJalan)
    elif(giliran == 'x'):
        arrayLegalMovesX.remove(tupleKoordinatJalan)
    else:
        return False

def jalan(posisi):
    global board,playTurn,koordinat
    koordinatJalan = posisi.split(",")
    if(isJalanLegal(playTurn,koordinatJalan[0],koordinatJalan[1])):
        board[int(koordinatJalan[0])][int(koordinatJalan[1])] = playTurn
        # Remove koordinatJalan dari arrayLegalMoves
        removeKoordinatDariArrayLegal(playTurn,int(koordinatJalan[0]),int(koordinatJalan[1]))
        # Mengganti giliran jalan
        if(playTurn == 'o'):
            playTurn = 'x'
        elif(playTurn =='x'):
            playTurn = 'o'
    else:
        # Koordinat tidak legal
        print("I'm sorry, but that move is invalid my friend. Please input another one. Which grid you want to play?")
        koordinat = input("")
        jalan(koordinat)

def isGridLegal(playTurn,baris,kolom):
    if(baris == 0 or baris == 10 or kolom == 0 or baris == 10):
        # Di luar papan
        return False
    elif(not isGridKosong(baris,kolom)):
        # Sudah terisi
        return False
    else:
        return True

def addArrayLegal(playTurn,baris,kolom):
    global arrayLegalMovesO,arrayLegalMovesX
    if playTurn=='o':
        arrayLegalMovesX.append((int(baris),int(kolom)))
    elif playTurn=='x':
        arrayLegalMovesO.append((int(baris),int(kolom)))
    else :
        print('Error')

def updateArrayLegalMove(playTurn,koordinat):
    # Lakukan pengecekan pada grid di sekitar koordinat input
    koordinatJalan = koordinat.split(",")
    # Kiri atas
    if isGridLegal(playTurn,int(koordinatJalan[0])-1, int(koordinatJalan[1])-1):
        addArrayLegal(playTurn, int(koordinatJalan[0])-1, int(koordinatJalan[1])-1)
    # Tengah atas
    if isGridLegal(playTurn,int(koordinatJalan[0])-1, int(koordinatJalan[1])):
        addArrayLegal(playTurn, int(koordinatJalan[0])-1, int(koordinatJalan[1]))
    # Kanan atas
    if isGridLegal(playTurn,int(koordinatJalan[0])-1, int(koordinatJalan[1])+1):
        addArrayLegal(playTurn, int(koordinatJalan[0])-1, int(koordinatJalan[1])+1)
    # Kiri
    if isGridLegal(playTurn,int(koordinatJalan[0]), int(koordinatJalan[1])-1):
        addArrayLegal(playTurn, int(koordinatJalan[0]), int(koordinatJalan[1])-1)
    # Kanan
    if isGridLegal(playTurn,int(koordinatJalan[0]), int(koordinatJalan[1])+1):
        addArrayLegal(playTurn, int(koordinatJalan[0]), int(koordinatJalan[1])+1)
    # Kiri bawah
    if isGridLegal(playTurn,int(koordinatJalan[0])+1, int(koordinatJalan[1])-1):
        addArrayLegal(playTurn, int(koordinatJalan[0])+1, int(koordinatJalan[1])-1)
    # Tengah bawah
    if isGridLegal(playTurn,int(koordinatJalan[0])+1, int(koordinatJalan[1])):
        addArrayLegal(playTurn, int(koordinatJalan[0])+1, int(koordinatJalan[1]))
    # Kanan bawah
    if isGridLegal(playTurn,int(koordinatJalan[0])+1, int(koordinatJalan[1])+1):
        addArrayLegal(playTurn, int(koordinatJalan[0])+1, int(koordinatJalan[1])+1)

    

arrayLegalMovesO = [(5,3),(6,4),(3,5),(4,6)]
arrayLegalMovesX = [(4,3),(3,4),(6,5),(5,6)]

gameEnd = 0
playTurn = 'o'

# MAIN

print("GAME BEGINS!")
while not gameEnd:
    showBoard(board)
    print("It's your turn player "+playTurn+", which grid you want to play?")
    koordinat = input("")
    jalan(koordinat)
    updateArrayLegalMove(playTurn,koordinat)

    # For checking purpose only. Delete if the project is finished.
    print('arrayLegalMovesO : ',arrayLegalMovesO)
    print('arrayLegalMovesX : ',arrayLegalMovesX)
    
