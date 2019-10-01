from board import *

def isJalanLegal(playTurn,baris,kolom,arrayLegalMovesO,arrayLegalMovesX):
    """Mengembalikan true jika board[baris][kolom] legal untuk
    ditandai playTurn(o atau x)"""

    tupleKoordinatJalan = (int(baris),int(kolom))
    if(playTurn == 'o'):
        return (tupleKoordinatJalan in arrayLegalMovesO)
    elif(playTurn == 'x'):
        return (tupleKoordinatJalan in arrayLegalMovesX)
    else:
        return False

def addArrayLegal(playTurn,baris,kolom, arrayLegalMovesO, arrayLegalMovesX):
    """Jika playTurn o add (baris,kolom) dari arrayLegalMovesX
    Jika playTurn x add (baris,kolom) dari arrayLegalMovesO"""
 
    if playTurn=='o':
        if((int(baris),int(kolom)) not in arrayLegalMovesX):
            arrayLegalMovesX.append((int(baris),int(kolom)))
    elif playTurn=='x':
        if((int(baris),int(kolom)) not in arrayLegalMovesO):
            arrayLegalMovesO.append((int(baris),int(kolom)))
    else :
        print('Error')

def updateArrayLegalMove(board, arrayLegalMovesO, arrayLegalMovesX):
    """Melakukan update arrayLegalMovesO dan arrayLegalMovesX
    sesuai dengan kondisi papan saat ini"""

    arrayLegalMovesO.clear()
    arrayLegalMovesX.clear()

    for i in range(1,9):
        for j in range(1,9):
            if isGridLegal(board,'o',i,j):
                addArrayLegal('o',i,j,arrayLegalMovesO,arrayLegalMovesX)
            if isGridLegal(board,'x',i,j):
                addArrayLegal('x',i,j, arrayLegalMovesO, arrayLegalMovesX)
    return((arrayLegalMovesO,arrayLegalMovesX))

def removeKoordinatDariArrayLegal(baris,kolom, arrayLegalMovesO, arrayLegalMovesX):
    """Jika playTurn o remove (baris,kolom) dari arrayLegalMovesX
    Jika playTurn x remove (baris,kolom) dari arrayLegalMovesO"""

    tupleKoordinatJalan = (int(baris),int(kolom))
    if(tupleKoordinatJalan in arrayLegalMovesO):
        arrayLegalMovesO.remove(tupleKoordinatJalan)
    if(tupleKoordinatJalan in arrayLegalMovesX):
        arrayLegalMovesX.remove(tupleKoordinatJalan)

def isGridLegal(board,playTurn,baris,kolom):
    """Tanya Timmy wkwkwkwk"""

    if(baris == 0 or baris == 9 or kolom == 0 or baris == 9):
        # Di luar papan
        return False
    elif(not isGridKosong(board,baris,kolom)):
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