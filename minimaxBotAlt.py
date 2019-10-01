from game import *
from evaluation import *
import copy

# TODO minimaxBot return tuple. Proses saat kembali ke depth sebelumnya
def minimaxBot(board, arrayLegalMovesO, arrayLegalMovesX, playTurn, depth, height):
    """Node pohon menggunakan AnyNode. Format = (id(board,legalO,legalX),nilaiEval,parent)"""
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
                # parent = copy.deepcopy(parentNode)
                stringJalan = str(i[0])+","+str(i[1])
                copyBoard = copy.deepcopy(jalan(initialBoard, stringJalan, playTurn, copy.deepcopy(arrayLegalMovesO), copy.deepcopy(arrayLegalMovesX)))
                if(playTurn == 'x'):
                    playTurnCheck = 'o'
                elif(playTurn == 'o'):
                    playTurnCheck = 'x'
                tupleArrayLegal = updateArrayLegalMove(copyBoard, copy.deepcopy(arrayLegalMovesO), copy.deepcopy(arrayLegalMovesX))

                # TODO simpan tuple langkah yang diambil di node
                # childNode = AnyNode(id=(copyBoard, tupleArrayLegal[0], tupleArrayLegal[1]), eval=0, parent=parentNode)
                
                hasil.append([(str(i[0]) + "," + str(i[1])),minimaxBot(copyBoard, tupleArrayLegal[0], tupleArrayLegal[1], playTurnCheck, depth-1, heightcopy)])
        
        else:
            hasil = []
            initialBoard = copy.deepcopy(board)
            # parent = copy.deepcopy(parentNode)
            copyBoard = copy.deepcopy(initialBoard)
            if(playTurn == 'x'):
                playTurnCheck = 'o'
            elif(playTurn == 'o'):
                playTurnCheck = 'x'
            tupleArrayLegal = updateArrayLegalMove(copyBoard, copy.deepcopy(arrayLegalMovesO), copy.deepcopy(arrayLegalMovesX))

            # TODO simpan tuple langkah yang diambil di node
            # childNode = Node((copyBoard, tupleArrayLegal[0], tupleArrayLegal[1]), eval=0, parent=parentNode)

            hasil.append(["0,0",minimaxBot(copyBoard, tupleArrayLegal[0], tupleArrayLegal[1], playTurnCheck, depth-1, heightcopy)])

        if (heightcopy != 1):
            if (heightcopy % 2 == 1): # ambil max
                temp = hasil[0][1]
                for x in hasil:
                    if (x[1] > temp):
                        temp = x[1]
                return hasil

            else: # ambil min
                temp = hasil[0][1]
                for x in hasil:
                    if (x[1] < temp):
                        temp = x[1]
                return hasil
        else:
            temp = hasil[0][1]
            woop = hasil[0][0]
            for x in hasil:
                if (x[1] > temp):
                    temp = x[1]
                    woop = x[0]
            return woop


# def evalTree(parentNode):
#     """Fungsi untuk memberi nilai eval pada daun pohon"""
#     queueId = []
#     for i in parentNode.children:
#         queueId.append(i)

# def minimaxBot(board, arrayLegalMovesO, arrayLegalMovesX, playTurn, depth):

# ---------------------------------------------Testing section------------------------------------------------------
# board = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]

# board[4][4] = 'o'
# board[4][5] = 'x'
# board[5][4] = 'x'
# board[5][5] = 'o'

# arrayLegalMovesO = [(5,3),(6,4),(3,5),(4,6)]
# arrayLegalMovesX = [(4,3),(3,4),(6,5),(5,6)]
# playTurn = 'o'
# depth = 6
# # parentNode = AnyNode(id=(board, arrayLegalMovesO, arrayLegalMovesX),eval=0)
# # print(RenderTree(parentNode))
# print(minimaxBot(board, arrayLegalMovesO, arrayLegalMovesX, playTurn, depth,0))

# test = parentNode
# while test.children:
#     test = test.children[0]

# print(test.eval)
# print(test.depth)

# # print(test.eval)

# # for i in range (0,len(parentNode.children)):
# #     print(parentNode.children[i])

# a = AnyNode(id = 'e')
# b = AnyNode(id = 'f',parent=a)
# c = AnyNode(id = 'g',parent=a)
# d = AnyNode(id = 'h',parent=b)


# print(len(b.siblings))
# # print(e)