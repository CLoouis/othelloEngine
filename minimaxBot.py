from game import *
from evaluation import *
from anytree import Node, RenderTree
import copy

def makeTree(board, arrayLegalMovesO, arrayLegalMovesX, playTurn, depth, parentNode):
    if(depth == 0):
        print("sampai di daun")
        # return
    else:
        if(playTurn == 'x'):    
            array = arrayLegalMovesX
        else:
            array = arrayLegalMovesO
        for i in array:
            initialBoard = copy.deepcopy(board)
            parent = copy.deepcopy(parentNode)
            print(depth)
            stringJalan = str(i[0])+","+str(i[1])
            print(stringJalan)
            copyBoard = copy.deepcopy(jalan(initialBoard, stringJalan, playTurn, copy.deepcopy(arrayLegalMovesO), copy.deepcopy(arrayLegalMovesX)))
            if(playTurn == 'x'):
                playTurnCheck = 'o'
            elif(playTurn == 'o'):
                playTurnCheck = 'x'
            tupleArrayLegal = updateArrayLegalMove(copyBoard, copy.deepcopy(arrayLegalMovesO), copy.deepcopy(arrayLegalMovesX))
            childNode = Node((copyBoard, tupleArrayLegal[0], tupleArrayLegal[1]), parent)
            
            makeTree(copyBoard, tupleArrayLegal[0], tupleArrayLegal[1], playTurnCheck, depth-1, childNode)
            

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
depth = 2
parentNode = Node((board, arrayLegalMovesO, arrayLegalMovesX))
# print(RenderTree(parentNode))
makeTree(board, arrayLegalMovesO, arrayLegalMovesX, playTurn, depth, parentNode)
print(RenderTree(parentNode))
