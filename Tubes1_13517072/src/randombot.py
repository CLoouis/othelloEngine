import random

def randomMove(arrayLegalO, arrayLegalX, playTurn):
    if (playTurn == 'o'):
        randomNum = random.randint(0, len(arrayLegalO) - 1)
        return arrayLegalO[randomNum]
    elif (playTurn == 'x'):
        randomNum = random.randint(0, len(arrayLegalX) - 1)
        return arrayLegalX[randomNum]
    else :
        return 'error'
