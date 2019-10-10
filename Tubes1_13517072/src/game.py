from legal import *

def jalan(board, posisi, playTurn, arrayLegalMovesO, arrayLegalMovesX):
    """Player menempatkan piece pada posisi di board"""

    koordinatJalan = posisi.split(",")
    if(isJalanLegal(playTurn,koordinatJalan[0],koordinatJalan[1],arrayLegalMovesO,arrayLegalMovesX)):
        board[int(koordinatJalan[0])][int(koordinatJalan[1])] = playTurn
        # Remove koordinatJalan dari arrayLegalMoves
        removeKoordinatDariArrayLegal(int(koordinatJalan[0]),int(koordinatJalan[1]),arrayLegalMovesO,arrayLegalMovesX)
        makanPiece(board, playTurn, posisi)
        return board
    else:
        # Koordinat tidak legal
        print("I'm sorry, but that move is invalid my friend. Please input another one. Which grid you want to play?")
        koordinat = input("")
        jalan(board,koordinat,playTurn, arrayLegalMovesO, arrayLegalMovesX)
        return board

def switchPlay(playTurn):
    """Mengganti playTurn dari o menjadi x atau dari x menjadi o
    karena variable primitive pass by value jadi perlu return"""

    if(playTurn == 'o'):
        playTurn = 'x'
    elif(playTurn == 'x'):
        playTurn = 'o'
    else:
        print('ERROR')
    return playTurn

def switchPiece(board,baris,kolom):
    """membalik piece board[baris][kolom]"""

    if(board[baris][kolom] == 'x'):
        board[baris][kolom] = 'o'
    elif(board[baris][kolom] == 'o'):
        board[baris][kolom] = 'x'

def makanPiece(board, playTurn, koordinat):
    """Tanya Timmy wkwkwkwk"""

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
                        switchPiece(board,indeksBaris,int(koordinatJalan[1]))
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
                        switchPiece(board,indeksBaris,indeksKolom)
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
                        switchPiece(board,indeksBaris,indeksKolom)
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
                        switchPiece(board,indeksBaris, indeksKolom)
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
                        switchPiece(board,indeksBaris,indeksKolom)
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
                        switchPiece(board,indeksBaris,indeksKolom)
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
                        switchPiece(board,indeksBaris,indeksKolom)
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
                        switchPiece(board,indeksBaris,indeksKolom)
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
                        switchPiece(board,indeksBaris,indeksKolom)
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
                        switchPiece(board,indeksBaris,indeksKolom)
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
                        switchPiece(board,indeksBaris,indeksKolom)
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
                        switchPiece(board,indeksBaris,indeksKolom)
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
                        switchPiece(board,indeksBaris,indeksKolom)
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
                        switchPiece(board,indeksBaris,indeksKolom)
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
                        switchPiece(board,indeksBaris,indeksKolom)
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
                        switchPiece(board,indeksBaris,indeksKolom)
                        indeksBaris = indeksBaris + 1
                        indeksKolom = indeksKolom + 1
                    break
                else:
                    indeksKolom = indeksKolom - 1
                    indeksBaris = indeksBaris - 1

def cekGameEnd(arrayLegalMovesO, arrayLegalMovesX):
    """True jika sudah tidak ada jalan yang bisa dilakukan kedua player"""

    return (arrayLegalMovesO == [] and arrayLegalMovesX == [])
