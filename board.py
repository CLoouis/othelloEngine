board = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#',' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]

board[4][4] = 'o'
board[4][5] = 'x'
board[5][4] = 'x'
board[5][5] = 'o'

global arrayLegalMovesO, arrayLegalMovesX, playTurn, koordinat
arrayLegalMovesO = [(5,3),(6,4),(3,5),(4,6)]
arrayLegalMovesX = [(4,3),(3,4),(6,5),(5,6)]
gameEnd = 0
playTurn = 'o'

def showBoard():
    """Menampilkan papan permainan saat ini"""

    global board
    print('    1   2   3   4   5   6   7   8')
    batas = '\n  ' + '+---'*8 + '+\n'
    ful = batas     
    for i in range(1, 9) :
        sebaris = str(i) + " | "
        for j in range(1, 9) :
            sebaris += board[i][j] + ' | '
        ful += sebaris + batas
    print(ful)

def isGridKosong(baris,kolom):
    """Mengembalikan true jika board[baris][kolom] kosong"""

    global board
    return (board[baris][kolom] == ' ')