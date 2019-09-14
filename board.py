board = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

def showBoard(board):
    """Show othello board based on board parameter"""
    batas = '\n' + '+---'*8 + '+\n'
    ful = batas     
    for i in range(8) :
        sebaris = "| "
        for j in range(8) :
            sebaris += board[i][j] + ' | '
        ful += sebaris + batas
    print(ful)

board[3][3] = 'o'
board[3][4] = 'x'
board[4][3] = 'x'
board[4][4] = 'o'
showBoard(board)