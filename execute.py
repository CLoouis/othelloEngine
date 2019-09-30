import randombot
# import minimaxBot

def execute(whoami, board, arrayLegalMovesO, arrayLegalMovesX, playTurn, depth):
    if (whoami == "1"):
        # player
        print("It's your turn player "+playTurn +
              ", which grid you want to play?")
        koordinat = input("")
        return koordinat
    elif (whoami == "2"):
        # random bot
        tupleMove = randombot.randomMove(arrayLegalMovesO, arrayLegalMovesX, playTurn)
        return str(tupleMove[0]) + ',' + str(tupleMove[1])
    elif (whoami == "3"):
        # minimax bot
        return 1,1
        # return minimaxBot.minimaxBot(board, arrayLegalMovesO, arrayLegalMovesX, playTurn, depth)
    else:
        return "error"
