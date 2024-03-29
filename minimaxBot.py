from game import *
from evaluation import *
from anytree import *
import copy


def chooseMaxNode(node):
    """Mengembalikan tuple (langkah,nilai eval) dari sebuah node dan siblings nya"""
    tempReturnNode = node
    for x in node.siblings:
        if(tempReturnNode.eval < x.eval):
            tempReturnNode = x
    return (tempReturnNode.langkah, tempReturnNode.eval)

def chooseMinNode(node):
    """Mengembalikan tuple (langkah,nilai eval) dari sebuah node dan siblings nya"""
    tempReturnNode = node
    for x in node.siblings:
        if(tempReturnNode.eval > x.eval):
            tempReturnNode = x
    return (tempReturnNode.langkah, tempReturnNode.eval)

# TODO makeTree return tuple. Proses saat kembali ke depth sebelumnya


def makeTree(board, arrayLegalMovesO, arrayLegalMovesX, playTurn, depth, parentNode):
    """Node pohon menggunakan AnyNode. Format = (id(board,legalO,legalX),nilaiEval,parent)"""
    # Basis
    if(depth == 1):
        if(playTurn == 'x'):    
            array = arrayLegalMovesX
        else:
            array = arrayLegalMovesO
        # Jika terdapat langkah legal
        if array:
            for i in array:
                initialBoard = copy.deepcopy(board)
                # parent = copy.deepcopy(parentNode)
                stringJalan = str(i[0])+","+str(i[1])
                copyBoard = copy.deepcopy(jalan(initialBoard, stringJalan, playTurn, copy.deepcopy(arrayLegalMovesO), copy.deepcopy(arrayLegalMovesX)))
                tupleArrayLegal = updateArrayLegalMove(copyBoard, copy.deepcopy(arrayLegalMovesO), copy.deepcopy(arrayLegalMovesX))
                evalValue = evalState(playTurn, copyBoard, tupleArrayLegal[0], tupleArrayLegal[1])
                childNode = AnyNode(id=(copyBoard, tupleArrayLegal[0], tupleArrayLegal[1]), eval=evalValue, parent=parentNode, langkah = i) 
            depthNode = parentNode.depth
            if (depthNode % 2 == 1):
                hasil = chooseMinNode(childNode)
            else:
                hasil = chooseMaxNode(childNode)
            parentNode.eval = hasil[1]
            return parentNode            
        else:
            initialBoard = copy.deepcopy(board)
            # parent = copy.deepcopy(parentNode)
            copyBoard = copy.deepcopy(initialBoard)
            tupleArrayLegal = updateArrayLegalMove(copyBoard, copy.deepcopy(arrayLegalMovesO), copy.deepcopy(arrayLegalMovesX))
            evalValue = evalState(playTurn, copyBoard, tupleArrayLegal[0], tupleArrayLegal[1])
            childNode = Node((copyBoard, tupleArrayLegal[0], tupleArrayLegal[1]), eval=evalValue, parent=parentNode, langkah = (0,0))
            depthNode = parentNode.depth
            if (depthNode % 2 == 1):
                hasil = chooseMinNode(childNode)
            else:
                hasil = chooseMaxNode(childNode)
            parentNode.eval = hasil[1]
            return parentNode
    elif(depth > 1):
        if(playTurn == 'x'):    
            array = arrayLegalMovesX
        else:
            array = arrayLegalMovesO
        # Jika terdapat langkah legal
        if array:
            for i in array:
                initialBoard = copy.deepcopy(board)
                # parent = copy.deepcopy(parentNode)
                stringJalan = str(i[0])+","+str(i[1])
                copyBoard = copy.deepcopy(jalan(initialBoard, stringJalan, playTurn, copy.deepcopy(arrayLegalMovesO), copy.deepcopy(arrayLegalMovesX)))
                if(playTurn == 'x'):
                    playTurnCheck = 'o'
                elif(playTurn == 'o'):
                    playTurnCheck = 'x'
                tupleArrayLegal = updateArrayLegalMove(copyBoard, copy.deepcopy(arrayLegalMovesO), copy.deepcopy(arrayLegalMovesX))
                childNode = AnyNode(id=(copyBoard, tupleArrayLegal[0], tupleArrayLegal[1]), eval=0, parent=parentNode, langkah = i)
                makeTree(copyBoard, tupleArrayLegal[0], tupleArrayLegal[1], playTurnCheck, depth-1, childNode)     
            if (parentNode.depth % 2 == 1):
                hasil = chooseMinNode(childNode)
            else:
                hasil = chooseMaxNode(childNode)
            parentNode.eval = hasil[1]
            return parentNode
        else:
            initialBoard = copy.deepcopy(board)
            # parent = copy.deepcopy(parentNode)
            copyBoard = copy.deepcopy(initialBoard)
            if(playTurn == 'x'):
                playTurnCheck = 'o'
            elif(playTurn == 'o'):
                playTurnCheck = 'x'
            tupleArrayLegal = updateArrayLegalMove(copyBoard, copy.deepcopy(arrayLegalMovesO), copy.deepcopy(arrayLegalMovesX))
            childNode = AnyNode(id=(copyBoard, tupleArrayLegal[0], tupleArrayLegal[1]), eval=0, parent=parentNode, langkah = (0,0))

            makeTree(copyBoard, tupleArrayLegal[0], tupleArrayLegal[1], playTurnCheck, depth-1, childNode)

            if (parentNode.depth % 2 == 1):
                hasil = chooseMinNode(childNode)
            else:
                hasil = chooseMaxNode(childNode)
            parentNode.eval = hasil[1]
            return parentNode
        

def minimaxBot(board, arrayLegalMovesO, arrayLegalMovesX, playTurn, depth):
    parentNode = AnyNode(id=(board, arrayLegalMovesO, arrayLegalMovesX), eval=0, langkah=(0, 0))
    hasil = makeTree(board,arrayLegalMovesO,arrayLegalMovesX,playTurn,depth,parentNode)
    for i in hasil.children:
        if(i.eval == parentNode.eval):
            return str(i.langkah[0])+","+str(i.langkah[1])

# ---------------------------------------------Testing section------------------------------------------------------
# board = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]

# board[4][4] = 'o'
# board[4][5] = 'x'
# board[5][4] = 'x'
# board[5][5] = 'o'

# arrayLegalMovesO = [(5,3),(6,4),(3,5),(4,6)]
# arrayLegalMovesX = [(4,3),(3,4),(6,5),(5,6)]
# playTurn = 'o'
# depth = 3
# parentNode = AnyNode(id=(board, arrayLegalMovesO, arrayLegalMovesX),eval=0, langkah=(0,0))
# # print(RenderTree(parentNode))
# nodeHasil = makeTree(board, arrayLegalMovesO, arrayLegalMovesX, playTurn, depth, parentNode)

# print(nodeHasil.eval)

# for i in range (0,len(parentNode.children)):
#     print(parentNode.children[i])

# a = AnyNode(id = 'e')
# b = AnyNode(id = 'f',parent=a)
# c = AnyNode(id = 'g',parent=a)
# d = AnyNode(id = 'h',parent=b)

# print(a.depth)
# print(e)
