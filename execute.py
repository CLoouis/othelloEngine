import randombot
import re
import legal
import minimaxBotAlt

def execute(whoami, board, arrayLegalMovesO, arrayLegalMovesX, playTurn, depth):
    if (whoami == "1"):
        # player
        print("It's your turn player "+playTurn +
              ", which grid you want to play?")
        print("Format: [# baris],[# kolom]")
        koordinat = input("")
        pattern = re.compile("^[0-9],[0-9]$")
        
        while True:
            if not(pattern.match(koordinat)):
                print("Format: [# baris],[# kolom]")
                koordinat = input("")
            else:
                koordinatJalan = koordinat.split(",")
                if legal.isJalanLegal(playTurn, koordinatJalan[0], koordinatJalan[1], arrayLegalMovesO, arrayLegalMovesX):
                    return koordinat
                else:
                    print("Input Tidak Valid")
                    koordinat = "2"
        
        

    elif (whoami == "2"):
        # random bot
        tupleMove = randombot.randomMove(arrayLegalMovesO, arrayLegalMovesX, playTurn)
        return str(tupleMove[0]) + ',' + str(tupleMove[1])
    elif (whoami == "3"):
        # minimax bot
        return minimaxBotAlt.minimaxBot(board, arrayLegalMovesO, arrayLegalMovesX, playTurn, 4, 0)
    else:
        return "error"
