# 1 = confesar
# 0 = mentir

beNice = True


def play(opponentMove):
    opponentHistory = []
    global beNice
    opponentHistory.append(opponentMove)
    if opponentMove == 'start':
        beNice = True
        opponentHistory.append(1)
        return 1
    if opponentHistory[-1] == 0:  # Se refiere al utlimo movimiento 
        beNice = False
    if beNice == True:
        return 1
    else:
        return 0


def name():
    return 'resentido'
