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

def isJalanLegal(baris,kolom):
    global arrayLegalMovesO,arrayLegalMovesX,playTurn
    tupleKoordinatJalan = (int(baris),int(kolom))
    if(playTurn == 'o'):
        return (tupleKoordinatJalan in arrayLegalMovesO)
    elif(playTurn == 'x'):
        return (tupleKoordinatJalan in arrayLegalMovesX)
    else:
        return False

def removeKoordinatDariArrayLegal(baris,kolom):
    global arrayLegalMovesO,arrayLegalMovesX
    tupleKoordinatJalan = (int(baris),int(kolom))
    if(tupleKoordinatJalan in arrayLegalMovesO):
        arrayLegalMovesO.remove(tupleKoordinatJalan)
    if(tupleKoordinatJalan in arrayLegalMovesX):
        arrayLegalMovesX.remove(tupleKoordinatJalan)

def jalan(posisi):
    global board,playTurn,koordinat
    koordinatJalan = posisi.split(",")
    if(isJalanLegal(koordinatJalan[0],koordinatJalan[1])):
        board[int(koordinatJalan[0])][int(koordinatJalan[1])] = playTurn
        # Remove koordinatJalan dari arrayLegalMoves
        removeKoordinatDariArrayLegal(int(koordinatJalan[0]),int(koordinatJalan[1]))
    else:
        # Koordinat tidak legal
        print("I'm sorry, but that move is invalid my friend. Please input another one. Which grid you want to play?")
        koordinat = input("")
        jalan(koordinat)

def isGridLegal(playTurn,baris,kolom):
    global board
    if(baris == 0 or baris == 9 or kolom == 0 or baris == 9):
        # Di luar papan
        return False
    elif(not isGridKosong(baris,kolom)):
        # Sudah terisi
        return False
    else:
        if(playTurn == 'x'):
            # Cek ke atas
            indeksBaris = baris
            indeksKolom = kolom
            
            # Cek apakah harus di cek ke atas
            if(board[indeksBaris-1][indeksKolom] == 'x'):
                while(indeksBaris > 0):
                    if(board[indeksBaris-1][indeksKolom] == 'o'):
                        # Ketemu temen
                        return True
                    elif(board[indeksBaris-1][indeksKolom] == ' '):
                        break
                    else:
                        indeksBaris = indeksBaris - 1

            # Cek ke kanan atas
            indeksBaris = baris
            indeksKolom = kolom
            
            # Cek apakah harus di cek ke kanan atas
            if(board[indeksBaris-1][indeksKolom+1] == 'x'):
                while(indeksBaris > 0 and indeksKolom < 9):
                    if(board[indeksBaris-1][indeksKolom+1] == 'o'):
                        return True
                    elif(board[indeksBaris-1][indeksKolom+1] == ' '):
                        break
                    else:
                        indeksBaris = indeksBaris - 1
                        indeksKolom = indeksKolom + 1

            # Cek ke kanan
            indeksBaris = baris
            indeksKolom = kolom
            
            # Cek apakah harus di cek ke kanan
            if(board[indeksBaris][indeksKolom+1] == 'x'):
                while(indeksKolom < 9):
                    if(board[indeksBaris][indeksKolom+1] == 'o'):
                        return True
                    elif(board[indeksBaris][indeksKolom+1] == ' '):
                        break
                    else:
                        indeksKolom = indeksKolom + 1

            # Cek ke kanan bawah
            indeksBaris = baris
            indeksKolom = kolom
            
            # Cek apakah harus di cek ke kanan bawah
            if(board[indeksBaris+1][indeksKolom+1] == 'x'):
                while(indeksBaris < 9 and indeksKolom < 9):
                    if(board[indeksBaris+1][indeksKolom+1] == 'o'):
                        return True
                    elif(board[indeksBaris+1][indeksKolom+1] == ' '):
                        break
                    else:
                        indeksKolom = indeksKolom + 1
                        indeksBaris = indeksBaris + 1

            # Cek ke bawah
            indeksBaris = baris
            indeksKolom = kolom
            
            # Cek apakah harus di cek ke bawah
            if(board[indeksBaris+1][indeksKolom] == 'x'):
                while(indeksBaris < 9):
                    if(board[indeksBaris+1][indeksKolom] == 'o'):
                        return True
                    elif(board[indeksBaris+1][indeksKolom] == ' '):
                        break
                    else:
                        indeksBaris = indeksBaris + 1

            # Cek ke kiri bawah
            indeksBaris = baris
            indeksKolom = kolom
            
            # Cek apakah harus di cek ke kiri bawah
            if(board[indeksBaris+1][indeksKolom-1] == 'x'):
                while(indeksBaris < 9 and indeksKolom > 0):
                    if(board[indeksBaris+1][indeksKolom-1] == 'o'):
                        return True
                    elif(board[indeksBaris+1][indeksKolom-1] == ' '):
                        break
                    else:
                        indeksBaris = indeksBaris + 1
                        indeksKolom = indeksKolom - 1

            # Cek ke kiri
            indeksBaris = baris
            indeksKolom = kolom
            
            # Cek apakah harus di cek ke kiri
            if(board[indeksBaris][indeksKolom-1] == 'x'):
                while(indeksKolom > 0):
                    if(board[indeksBaris][indeksKolom-1] == 'o'):
                        return True
                    elif(board[indeksBaris][indeksKolom-1] == ' '):
                        break
                    else:
                        indeksKolom = indeksKolom - 1

            # Cek ke kiri atas
            indeksBaris = baris
            indeksKolom = kolom
            
            # Cek apakah harus di cek ke kiri atas
            if(board[indeksBaris-1][indeksKolom-1] == 'x'):
                while(indeksBaris > 0 and indeksKolom > 0):
                    if(board[indeksBaris-1][indeksKolom-1] == 'o'):
                        return True
                    elif(board[indeksBaris-1][indeksKolom-1] == ' '):
                        break
                    else:
                        indeksKolom = indeksKolom - 1
                        indeksBaris = indeksBaris - 1
            
            return False
            
        elif(playTurn == 'o'):
            # Cek ke atas
            indeksBaris = baris
            indeksKolom = kolom
            
            # Cek apakah harus di cek ke atas
            if(board[indeksBaris-1][indeksKolom] == 'o'):
                while(indeksBaris > 0):
                    if(board[indeksBaris-1][indeksKolom] == 'x'):
                        # Ketemu temen
                        return True
                    elif(board[indeksBaris-1][indeksKolom] == ' '):
                        break
                    else:
                        indeksBaris = indeksBaris - 1

            # Cek ke kanan atas
            indeksBaris = baris
            indeksKolom = kolom
            
            # Cek apakah harus di cek ke kanan atas
            if(board[indeksBaris-1][indeksKolom+1] == 'o'):
                while(indeksBaris > 0 and indeksKolom < 9):
                    if(board[indeksBaris-1][indeksKolom+1] == 'x'):
                        return True
                    elif(board[indeksBaris-1][indeksKolom+1] == ' '):
                        break
                    else:
                        indeksBaris = indeksBaris - 1
                        indeksKolom = indeksKolom + 1

            # Cek ke kanan
            indeksBaris = baris
            indeksKolom = kolom
            
            # Cek apakah harus di cek ke kanan
            if(board[indeksBaris][indeksKolom+1] == 'o'):
                while(indeksKolom < 9):
                    if(board[indeksBaris][indeksKolom+1] == 'x'):
                        return True
                    elif(board[indeksBaris][indeksKolom+1] == ' '):
                        break
                    else:
                        indeksKolom = indeksKolom + 1

            # Cek ke kanan bawah
            indeksBaris = baris
            indeksKolom = kolom
            
            # Cek apakah harus di cek ke kanan bawah
            if(board[indeksBaris+1][indeksKolom+1] == 'o'):
                while(indeksBaris < 9 and indeksKolom < 9):
                    if(board[indeksBaris+1][indeksKolom+1] == 'x'):
                        return True
                    elif(board[indeksBaris+1][indeksKolom+1] == ' '):
                        break
                    else:
                        indeksKolom = indeksKolom + 1
                        indeksBaris = indeksBaris + 1

            # Cek ke bawah
            indeksBaris = baris
            indeksKolom = kolom
            
            # Cek apakah harus di cek ke bawah
            if(board[indeksBaris+1][indeksKolom] == 'o'):
                while(indeksBaris < 9):
                    if(board[indeksBaris+1][indeksKolom] == 'x'):
                        return True
                    elif(board[indeksBaris+1][indeksKolom] == ' '):
                        break
                    else:
                        indeksBaris = indeksBaris + 1

            # Cek ke kiri bawah
            indeksBaris = baris
            indeksKolom = kolom
            
            # Cek apakah harus di cek ke kiri bawah
            if(board[indeksBaris+1][indeksKolom-1] == 'o'):
                while(indeksBaris < 9 and indeksKolom > 0):
                    if(board[indeksBaris+1][indeksKolom-1] == 'x'):
                        return True
                    elif(board[indeksBaris+1][indeksKolom-1] == ' '):
                        break
                    else:
                        indeksBaris = indeksBaris + 1
                        indeksKolom = indeksKolom - 1

            # Cek ke kiri
            indeksBaris = baris
            indeksKolom = kolom
            
            # Cek apakah harus di cek ke kiri
            if(board[indeksBaris][indeksKolom-1] == 'o'):
                while(indeksKolom > 0):
                    if(board[indeksBaris][indeksKolom-1] == 'x'):
                        return True
                    elif(board[indeksBaris][indeksKolom-1] == ' '):
                        break
                    else:
                        indeksKolom = indeksKolom - 1

            # Cek ke kiri atas
            indeksBaris = baris
            indeksKolom = kolom
            
            # Cek apakah harus di cek ke kiri atas
            if(board[indeksBaris-1][indeksKolom-1] == 'o'):
                while(indeksBaris > 0 and indeksKolom > 0):
                    if(board[indeksBaris-1][indeksKolom-1] == 'x'):
                        return True
                    elif(board[indeksBaris-1][indeksKolom-1] == ' '):
                        break
                    else:
                        indeksKolom = indeksKolom - 1
                        indeksBaris = indeksBaris - 1
            
            return False


def addArrayLegal(playTurn,baris,kolom):
    global arrayLegalMovesO,arrayLegalMovesX
    if playTurn=='o':
        if((int(baris),int(kolom)) not in arrayLegalMovesX):
            arrayLegalMovesX.append((int(baris),int(kolom)))
    elif playTurn=='x':
        if((int(baris),int(kolom)) not in arrayLegalMovesO):
            arrayLegalMovesO.append((int(baris),int(kolom)))
    else :
        print('Error')

def updateArrayLegalMove():
    global playTurn,arrayLegalMovesO,arrayLegalMovesX
    arrayLegalMovesO = []
    arrayLegalMovesX = []
    for i in range(1,9):
        for j in range(1,9):
            if isGridLegal('o',i,j):
                addArrayLegal('o',i,j)
            if isGridLegal('x',i,j):
                addArrayLegal('x',i,j)


def switchPlay():
    global playTurn
    if(playTurn == 'o'):
        playTurn = 'x'
    elif(playTurn == 'x'):
        playTurn = 'o'
    else:
        print('ERROR')

def switchPiece(baris,kolom):
    global board
    if(board[baris][kolom] == 'x'):
        board[baris][kolom] = 'o'
    elif(board[baris][kolom] == 'o'):
        board[baris][kolom] = 'x'

def makanPiece(koordinat):
    global playTurn
    koordinatJalan = koordinat.split(",")
    if(playTurn == 'o'):
        # Cek ke atas

        indeksBaris = int(koordinatJalan[0])
        indeksKolom = int(koordinatJalan[1])
        
        # Cek apakah harus di cek ke atas
        if(board[indeksBaris-1][indeksKolom] == 'x'):
            while(indeksBaris > 0):
                if(board[indeksBaris-1][indeksKolom] == 'o'):
                    # Ketemu temen
                    while indeksBaris < int(koordinatJalan[0]):
                        switchPiece(indeksBaris,int(koordinatJalan[1]))
                        indeksBaris = indeksBaris + 1
                    break
                else:
                    indeksBaris = indeksBaris - 1

        # Cek ke kanan atas
        indeksBaris = int(koordinatJalan[0])
        indeksKolom = int(koordinatJalan[1])
        
        # Cek apakah harus di cek ke kanan atas
        if(board[indeksBaris-1][indeksKolom+1] == 'x'):
            while(indeksBaris > 0 and indeksKolom < 9):
                if(board[indeksBaris-1][indeksKolom+1] == 'o'):
                    # Ketemu temen
                    while indeksBaris < int(koordinatJalan[0]) and indeksKolom > int(koordinatJalan[1]):
                        switchPiece(indeksBaris,indeksKolom)
                        indeksBaris = indeksBaris + 1
                        indeksKolom = indeksKolom - 1
                    break
                else:
                    indeksBaris = indeksBaris - 1
                    indeksKolom = indeksKolom + 1

        # Cek ke kanan
        indeksBaris = int(koordinatJalan[0])
        indeksKolom = int(koordinatJalan[1])
        
        # Cek apakah harus di cek ke kanan
        if(board[indeksBaris][indeksKolom+1] == 'x'):
            while(indeksKolom < 9):
                if(board[indeksBaris][indeksKolom+1] == 'o'):
                    # Ketemu temen
                    while indeksKolom > int(koordinatJalan[1]):
                        switchPiece(indeksBaris,indeksKolom)
                        indeksKolom = indeksKolom - 1
                    break
                else:
                    indeksKolom = indeksKolom + 1

        # Cek ke kanan bawah
        indeksBaris = int(koordinatJalan[0])
        indeksKolom = int(koordinatJalan[1])
        
        # Cek apakah harus di cek ke kanan bawah
        if(board[indeksBaris+1][indeksKolom+1] == 'x'):
            while(indeksBaris < 9 and indeksKolom < 9):
                if(board[indeksBaris+1][indeksKolom+1] == 'o'):
                    # Ketemu temen
                    while indeksBaris > int(koordinatJalan[0]) and indeksKolom > int(koordinatJalan[1]):
                        switchPiece(indeksBaris, indeksKolom)
                        indeksBaris = indeksBaris - 1
                        indeksKolom = indeksKolom - 1
                    break
                else:
                    indeksKolom = indeksKolom + 1
                    indeksBaris = indeksBaris + 1

        # Cek ke bawah
        indeksBaris = int(koordinatJalan[0])
        indeksKolom = int(koordinatJalan[1])
        
        # Cek apakah harus di cek ke bawah
        if(board[indeksBaris+1][indeksKolom] == 'x'):
            while(indeksBaris < 9):
                if(board[indeksBaris+1][indeksKolom] == 'o'):
                    # Ketemu temen
                    while indeksBaris > int(koordinatJalan[0]):
                        switchPiece(indeksBaris,indeksKolom)
                        indeksBaris = indeksBaris - 1
                    break
                else:
                    indeksBaris = indeksBaris + 1

        # Cek ke kiri bawah
        indeksBaris = int(koordinatJalan[0])
        indeksKolom = int(koordinatJalan[1])
        
        # Cek apakah harus di cek ke kiri bawah
        if(board[indeksBaris+1][indeksKolom-1] == 'x'):
            while(indeksBaris < 9 and indeksKolom > 0):
                if(board[indeksBaris+1][indeksKolom-1] == 'o'):
                    # Ketemu temen
                    while indeksBaris > int(koordinatJalan[0]) and indeksKolom < int(koordinatJalan[1]):
                        switchPiece(indeksBaris,indeksKolom)
                        indeksBaris = indeksBaris - 1
                        indeksKolom = indeksKolom + 1
                    break
                else:
                    indeksBaris = indeksBaris + 1
                    indeksKolom = indeksKolom - 1

        # Cek ke kiri
        indeksBaris = int(koordinatJalan[0])
        indeksKolom = int(koordinatJalan[1])
        
        # Cek apakah harus di cek ke kiri
        if(board[indeksBaris][indeksKolom-1] == 'x'):
            while(indeksKolom > 0):
                if(board[indeksBaris][indeksKolom-1] == 'o'):
                    # Ketemu temen
                    while indeksKolom < int(koordinatJalan[1]):
                        switchPiece(indeksBaris,indeksKolom)
                        indeksKolom = indeksKolom + 1
                    break
                else:
                    indeksKolom = indeksKolom - 1

        # Cek ke kiri atas
        indeksBaris = int(koordinatJalan[0])
        indeksKolom = int(koordinatJalan[1])
        
        # Cek apakah harus di cek ke kiri atas
        if(board[indeksBaris-1][indeksKolom-1] == 'x'):
            while(indeksBaris > 0 and indeksKolom > 0):
                if(board[indeksBaris-1][indeksKolom-1] == 'o'):
                    # Ketemu temen
                    while indeksBaris < int(koordinatJalan[0]) and indeksKolom < int(koordinatJalan[1]):
                        switchPiece(indeksBaris,indeksKolom)
                        indeksBaris = indeksBaris + 1
                        indeksKolom = indeksKolom + 1
                    break
                else:
                    indeksKolom = indeksKolom - 1
                    indeksBaris = indeksBaris - 1
                
    elif(playTurn == 'x'):
        # Cek ke atas

        indeksBaris = int(koordinatJalan[0])
        indeksKolom = int(koordinatJalan[1])
        
        # Cek apakah harus di cek ke atas
        if(board[indeksBaris-1][indeksKolom] == 'o'):
            while(indeksBaris > 0):
                if(board[indeksBaris-1][indeksKolom] == 'x'):
                    # Ketemu temen
                    while indeksBaris < int(koordinatJalan[0]):
                        switchPiece(indeksBaris,indeksKolom)
                        indeksBaris = indeksBaris + 1
                    break
                else:
                    indeksBaris = indeksBaris - 1

        # Cek ke kanan atas
        indeksBaris = int(koordinatJalan[0])
        indeksKolom = int(koordinatJalan[1])
        
        # Cek apakah harus di cek ke kanan atas
        if(board[indeksBaris-1][indeksKolom+1] == 'o'):
            while(indeksBaris > 0 and indeksKolom < 9):
                if(board[indeksBaris-1][indeksKolom+1] == 'x'):
                    # Ketemu temen
                    while indeksBaris < int(koordinatJalan[0]) and indeksKolom > int(koordinatJalan[1]):
                        switchPiece(indeksBaris,indeksKolom)
                        indeksBaris = indeksBaris + 1
                        indeksKolom = indeksKolom - 1
                    break
                else:
                    indeksBaris = indeksBaris - 1
                    indeksKolom = indeksKolom + 1

        # Cek ke kanan
        indeksBaris = int(koordinatJalan[0])
        indeksKolom = int(koordinatJalan[1])
        
        # Cek apakah harus di cek ke kanan
        if(board[indeksBaris][indeksKolom+1] == 'o'):
            while(indeksKolom < 9):
                if(board[indeksBaris][indeksKolom+1] == 'x'):
                    # Ketemu temen
                    while indeksKolom > int(koordinatJalan[1]):
                        switchPiece(indeksBaris,indeksKolom)
                        indeksKolom = indeksKolom - 1
                    break
                else:
                    indeksKolom = indeksKolom + 1

        # Cek ke kanan bawah
        indeksBaris = int(koordinatJalan[0])
        indeksKolom = int(koordinatJalan[1])
        
        # Cek apakah harus di cek ke kanan bawah
        if(board[indeksBaris+1][indeksKolom+1] == 'o'):
            while(indeksBaris < 9 and indeksKolom < 9):
                if(board[indeksBaris+1][indeksKolom+1] == 'x'):
                    # Ketemu temen
                    while indeksBaris > int(koordinatJalan[0]) and indeksKolom > int(koordinatJalan[1]):
                        switchPiece(indeksBaris,indeksKolom)
                        indeksBaris = indeksBaris - 1
                        indeksKolom = indeksKolom - 1
                    break
                else:
                    indeksKolom = indeksKolom + 1
                    indeksBaris = indeksBaris + 1

        # Cek ke bawah
        indeksBaris = int(koordinatJalan[0])
        indeksKolom = int(koordinatJalan[1])
        
        # Cek apakah harus di cek ke bawah
        if(board[indeksBaris+1][indeksKolom] == 'o'):
            while(indeksBaris < 9):
                if(board[indeksBaris+1][indeksKolom] == 'x'):
                    # Ketemu temen
                    while indeksBaris > int(koordinatJalan[0]):
                        switchPiece(indeksBaris,indeksKolom)
                        indeksBaris = indeksBaris - 1
                    break
                else:
                    indeksBaris = indeksBaris + 1

        # Cek ke kiri bawah
        indeksBaris = int(koordinatJalan[0])
        indeksKolom = int(koordinatJalan[1])
        
        # Cek apakah harus di cek ke kiri bawah
        if(board[indeksBaris+1][indeksKolom-1] == 'o'):
            while(indeksBaris < 9 and indeksKolom > 0):
                if(board[indeksBaris+1][indeksKolom-1] == 'x'):
                    # Ketemu temen
                    while indeksBaris > int(koordinatJalan[0]) and indeksKolom < int(koordinatJalan[1]):
                        switchPiece(indeksBaris,indeksKolom)
                        indeksBaris = indeksBaris - 1
                        indeksKolom = indeksKolom + 1
                    break
                else:
                    indeksBaris = indeksBaris + 1
                    indeksKolom = indeksKolom - 1

        # Cek ke kiri
        indeksBaris = int(koordinatJalan[0])
        indeksKolom = int(koordinatJalan[1])
        
        # Cek apakah harus di cek ke kiri
        if(board[indeksBaris][indeksKolom-1] == 'o'):
            while(indeksKolom > 0):
                if(board[indeksBaris][indeksKolom-1] == 'x'):
                    # Ketemu temen
                    while indeksKolom < int(koordinatJalan[1]):
                        switchPiece(indeksBaris,indeksKolom)
                        indeksKolom = indeksKolom + 1
                    break
                else:
                    indeksKolom = indeksKolom - 1

        # Cek ke kiri atas
        indeksBaris = int(koordinatJalan[0])
        indeksKolom = int(koordinatJalan[1])
        
        # Cek apakah harus di cek ke kiri atas
        if(board[indeksBaris-1][indeksKolom-1] == 'o'):
            while(indeksBaris > 0 and indeksKolom > 0):
                if(board[indeksBaris-1][indeksKolom-1] == 'x'):
                    # Ketemu temen
                    while indeksBaris < int(koordinatJalan[0]) and indeksKolom < int(koordinatJalan[1]):
                        switchPiece(indeksBaris,indeksKolom)
                        indeksBaris = indeksBaris + 1
                        indeksKolom = indeksKolom + 1
                    break
                else:
                    indeksKolom = indeksKolom - 1
                    indeksBaris = indeksBaris - 1
        
    
def cekGameEnd():
    global arrayLegalMovesO, arrayLegalMovesX
    # Tidak ada yang bisa jalan
    return (arrayLegalMovesO == [] and arrayLegalMovesX == [])

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
    if(playTurn == 'o'):
        if(arrayLegalMovesO):
            print("It's your turn player "+playTurn+", which grid you want to play?")
            koordinat = input("")
            jalan(koordinat)
            makanPiece(koordinat)
            updateArrayLegalMove()
        else:
            print("Sorry my friend, there is no legal move for you this turn")
    elif(playTurn == 'x'):
        if(arrayLegalMovesX):
            print("It's your turn player "+playTurn+", which grid you want to play?")
            koordinat = input("")
            jalan(koordinat)
            makanPiece(koordinat)
            updateArrayLegalMove()
        else:
            print("Sorry my friend, there is no legal move for you this turn")
    
    gameEnd = cekGameEnd()
    switchPlay()

    # For checking purpose only. Delete if the project is finished.
    print('arrayLegalMovesO : ',arrayLegalMovesO)
    print('arrayLegalMovesX : ',arrayLegalMovesX)
    
