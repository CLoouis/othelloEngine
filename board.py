board = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]

def showBoard(board):
    """Menampilkan papan permainan saat ini"""
    print('    1   2   3   4   5   6   7   8')
    batas = '\n  ' + '+---'*8 + '+\n'
    ful = batas     
    for i in range(1, 9) :
        sebaris = str(i) + " | "
        for j in range(1, 9) :
            sebaris += board[i][j] + ' | '
        ful += sebaris + batas
    print(ful)

board[4][4] = 'o'
board[4][5] = 'x'
board[5][4] = 'x'
board[5][5] = 'o'

global arrayLegalMovesO, arrayLegalMovesX, playTurn
arrayLegalMovesO = [(4,2),(5,3),(2,4),(3,5)]
arrayLegalMovesX = [(3,2),(2,3),(5,4),(4,5)]

