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

def isGridKosong(board, baris,kolom):
    """Mengembalikan true jika board[baris][kolom] kosong"""

    return (board[baris][kolom] == ' ')

def countScore(board):
    countO = 0
    countX = 0

    for i in range(1,9):
        for j in range(1,9):
            if (board[i][j] == 'o'):
                countO += 1
            elif (board[i][j] == 'x'):
                countX += 1
    
    print("Number of O = ", countO)
    print("Number of X = ", countX)