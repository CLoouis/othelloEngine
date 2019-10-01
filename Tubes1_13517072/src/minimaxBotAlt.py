from game import *
from evaluation import *
import copy

def minimaxBot(board, arrayLegalMovesO, arrayLegalMovesX, playTurn, depth, height, alpha, beta):
    """Node pohon menggunakan AnyNode. Format = (id(board,legalO,legalX),nilaiEval,parent)"""
    alphalocal = copy.deepcopy(alpha)
    betalocal = copy.deepcopy(beta)
    # Basis
    if(depth == 0):
        return evalState(playTurn, board, arrayLegalMovesO, arrayLegalMovesX)

    elif(depth >= 1):
        heightcopy = height + 1
        if(playTurn == 'x'):    
            array = arrayLegalMovesX
        else:
            array = arrayLegalMovesO
        # Jika terdapat langkah legal
        if array:
            for i in array:
                hasil = []
                initialBoard = copy.deepcopy(board)
                stringJalan = str(i[0])+","+str(i[1])
                copyBoard = copy.deepcopy(jalan(initialBoard, stringJalan, playTurn, copy.deepcopy(arrayLegalMovesO), copy.deepcopy(arrayLegalMovesX)))
                if(playTurn == 'x'):
                    playTurnCheck = 'o'
                elif(playTurn == 'o'):
                    playTurnCheck = 'x'
                tupleArrayLegal = updateArrayLegalMove(copyBoard, copy.deepcopy(arrayLegalMovesO), copy.deepcopy(arrayLegalMovesX))

                value = minimaxBot(
                    copyBoard, tupleArrayLegal[0], tupleArrayLegal[1], playTurnCheck, depth-1, heightcopy, alphalocal, betalocal)
                hasil.append([(str(i[0]) + "," + str(i[1])),value])
                if (heightcopy % 2 == 1):  # ambil max
                    alphalocal = max(alphalocal, value)
                else:  # ambil min
                    betalocal = min(betalocal, value)
                if (alphalocal >= betalocal):
                    break
        else:
            hasil = []
            initialBoard = copy.deepcopy(board)
            copyBoard = copy.deepcopy(initialBoard)
            if(playTurn == 'x'):
                playTurnCheck = 'o'
            elif(playTurn == 'o'):
                playTurnCheck = 'x'
            tupleArrayLegal = updateArrayLegalMove(copyBoard, copy.deepcopy(arrayLegalMovesO), copy.deepcopy(arrayLegalMovesX))
            hasil.append(["0,0", minimaxBot(copyBoard, tupleArrayLegal[0], tupleArrayLegal[1],
                                            playTurnCheck, depth-1, heightcopy, alphalocal, betalocal)])

        if (heightcopy != 1):
            if (heightcopy % 2 == 1): # ambil max
                temp = hasil[0][1]
                for x in hasil:
                    if (x[1] > temp):
                        temp = x[1]
                return temp

            else: # ambil min
                temp = hasil[0][1]
                for x in hasil:
                    if (x[1] < temp):
                        temp = x[1]
                return temp
        else:
            temp = hasil[0][1]
            woop = hasil[0][0]
            for x in hasil:
                if (x[1] > temp):
                    temp = x[1]
                    woop = x[0]
            return woop
