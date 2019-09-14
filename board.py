board = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

def showBoard(board):
    """Show othello board based on board parameter"""
    print('    0   1   2   3   4   5   6   7')
    batas = '\n  ' + '+---'*8 + '+\n'
    ful = batas     
    for i in range(8) :
        sebaris = str(i) + " | "
        for j in range(8) :
            sebaris += board[i][j] + ' | '
        ful += sebaris + batas
    print(ful)

board[3][3] = 'o'
board[3][4] = 'x'
board[4][3] = 'x'
board[4][4] = 'o'
# showBoard(board)

# def main():
#     while (True):
#         baris = int(input("Silahkan pilih baris : "))
#         kolom = int(input("Silahkan pilih kolom : "))

#         board[baris][kolom] = 'o'

#         showBoard(board)

# main()