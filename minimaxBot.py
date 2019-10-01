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
    return tempReturnNode

def chooseMinNode(node):
    """Mengembalikan tuple (langkah,nilai eval) dari sebuah node dan siblings nya"""
    tempReturnNode = node
    for x in node.siblings:
        if(tempReturnNode.eval > x.eval):
            tempReturnNode = x
    return tempReturnNode

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
                childNode = AnyNode(id=(copyBoard, tupleArrayLegal[0], tupleArrayLegal[1]), eval=evalValue, parent=parentNode)
        else:
            initialBoard = copy.deepcopy(board)
            # parent = copy.deepcopy(parentNode)
            copyBoard = copy.deepcopy(initialBoard)
            tupleArrayLegal = updateArrayLegalMove(copyBoard, copy.deepcopy(arrayLegalMovesO), copy.deepcopy(arrayLegalMovesX))
            evalValue = evalState(playTurn, copyBoard, tupleArrayLegal[0], tupleArrayLegal[1])
            childNode = Node((copyBoard, tupleArrayLegal[0], tupleArrayLegal[1]), parent=parentNode)
            return((0,0),evalValue)
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

                # TODO simpan tuple langkah yang diambil di node
                childNode = AnyNode(id=(copyBoard, tupleArrayLegal[0], tupleArrayLegal[1]), eval=0, parent=parentNode)
                
                makeTree(copyBoard, tupleArrayLegal[0], tupleArrayLegal[1], playTurnCheck, depth-1, childNode)
        else:
            initialBoard = copy.deepcopy(board)
            # parent = copy.deepcopy(parentNode)
            copyBoard = copy.deepcopy(initialBoard)
            if(playTurn == 'x'):
                playTurnCheck = 'o'
            elif(playTurn == 'o'):
                playTurnCheck = 'x'
            tupleArrayLegal = updateArrayLegalMove(copyBoard, copy.deepcopy(arrayLegalMovesO), copy.deepcopy(arrayLegalMovesX))

            # TODO simpan tuple langkah yang diambil di node
            childNode = Node((copyBoard, tupleArrayLegal[0], tupleArrayLegal[1]), parent=parentNode)

            makeTree(copyBoard, tupleArrayLegal[0], tupleArrayLegal[1], playTurnCheck, depth-1, childNode)
        
# def evalTree(parentNode):
#     """Fungsi untuk memberi nilai eval pada daun pohon"""
#     queueId = []
#     for i in parentNode.children:
#         queueId.append(i)

# def minimaxBot(board, arrayLegalMovesO, arrayLegalMovesX, playTurn, depth):

# ---------------------------------------------Testing section------------------------------------------------------
board = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]

board[4][4] = 'o'
board[4][5] = 'x'
board[5][4] = 'x'
board[5][5] = 'o'

arrayLegalMovesO = [(5,3),(6,4),(3,5),(4,6)]
arrayLegalMovesX = [(4,3),(3,4),(6,5),(5,6)]
playTurn = 'o'
depth = 4
parentNode = AnyNode(id=(board, arrayLegalMovesO, arrayLegalMovesX),eval=0)
# print(RenderTree(parentNode))
makeTree(board, arrayLegalMovesO, arrayLegalMovesX, playTurn, depth, parentNode)

test = parentNode
while test.children:
    test = test.children[0]

print(test.eval)
print(test.depth)

# print(test.eval)

# for i in range (0,len(parentNode.children)):
#     print(parentNode.children[i])

a = AnyNode(id = 'e')
b = AnyNode(id = 'f',parent=a)
c = AnyNode(id = 'g',parent=a)
d = AnyNode(id = 'h',parent=b)


print(len(b.siblings))
# print(e)