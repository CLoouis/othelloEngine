def evalCoinParityEvaluation(playTurn, board):
    """Menghitung perbandingan banyaknya piece milik sendiri 
    dibanding dengan milik musuh"""

    numberOfPlayTurnPiece = 0
    numberOfEnemiesPiece = 0

    for i in range(1, 9):
        for j in range(1, 9):
            if (board[i][j] == playTurn):
                numberOfPlayTurnPiece += 1
            elif (board[i][j] != ' ') :
                numberOfEnemiesPiece += 1
    
    return numberOfPlayTurnPiece - numberOfEnemiesPiece



def mobilityEvaluation(playTurn, arrayLegalMovesO, arrayLegalMovesX):
    """Menghitung perbandingan banyaknya kemungkinan jalan dari turn pemain
    saat ini dan turn pemain berikutnya"""

    if (playTurn == 'o'):
        return len(arrayLegalMovesO) - len(arrayLegalMovesX)
    else :
        return len(arrayLegalMovesX) - len(arrayLegalMovesO)


WeightHeuristicBoard = [
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0] , 
    [0 , 10 , -5 , 3 , 3 , 3 , 3 , -5 , 10 , 0] , 
    [0 , -5 , -3 , -1 , -1 , -1 , -1 , -3 , -5 , 0] , 
    [0 , 3 , -1 , 1 , 0 , 0 , 1 , -1 , 3 , 0] , 
    [0 , 3 , -1 , 0 , 1 , 1 , 0 , -1 , 3 , 0] , 
    [0 , 3 , -1 , 0 , 1 , 1 , 0 , -1 , 3 , 0] , 
    [0 , 3 , -1 , 1 , 0 , 0 , 1 , -1 , 3 , 0] , 
    [0 , -5 , -3 , -1 , -1 , -1 , -1 , -3 , -5 , 0] , 
    [0 , 10 , -5 , 3 , 3 , 3 , 3 , -5 , 10 , 0] , 
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0]
]

def stabilityEvaluation(playTurn ,  board):
    """Mengembalikan nilai evaluasi berdasarkan posisi piece"""

    nilaiStabilityPlayer = 0
    nilaiStabilityEnemy = 0

    for i in range(1,9):
        for j in range(1,9):
            if (board[i][j] == playTurn):
                nilaiStabilityPlayer += WeightHeuristicBoard[i][j]
            elif (board[i][j] != ' '):
                nilaiStabilityEnemy += WeightHeuristicBoard[i][j]
    
    return nilaiStabilityPlayer - nilaiStabilityEnemy

def evalState(playTurn, board, arrayLegalMovesO, arrayLegalMovesX):
    """Mengembalikan nilai evaluasi dari sebuah susunan papan (board)
    pada sebuah giliran tertentu"""

    return  evalCoinParityEvaluation(playTurn, board) + mobilityEvaluation(playTurn, arrayLegalMovesO, arrayLegalMovesX) + stabilityEvaluation(playTurn, board)

