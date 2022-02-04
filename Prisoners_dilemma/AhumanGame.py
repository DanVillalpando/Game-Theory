import SiempreConfesar, SiempreMentir, titForTat, AleatorioBasic, ConfesarAleatorio, MentirAleatorio, \
    Resentido, pavlov, ES, myStrategy

strategies = [SiempreConfesar, SiempreMentir, titForTat, AleatorioBasic, ConfesarAleatorio, MentirAleatorio, \
    Resentido, pavlov, ES, myStrategy]


def play(AI, rounds):
    print('Hola humano, soy una AI. Cual es tu nombre? ')
    yourName = input()
    print('Humano contra ', AI.name())
    global scores
    yourScore = 0
    AIscore = 0

    print('presiona 1 to confesar o 0 para mentir ')
    yourMove = int(input())
    AImove = AI.play('start')

    for i in range(rounds):
        if yourMove == 1 and AImove == 1:
            yourScore += 1
            AIscore += 1
            print('empate')
        elif yourMove == 1 and AImove == 0:
            AIscore += 2
            print(AI.name(), 'mintio y gano')
        elif yourMove == 0 and AImove == 1:
            yourScore += 2
            print('tu mentiste y ganaste')
        else:
            print('ambos mintieron')
        print('presiona 1 to confesar o 0 para mentir ')
        yourPrevMove = yourMove
        yourMove = int(input())
        AImove = AI.play(yourPrevMove)
    if yourScore > AIscore:
        print(yourName, 'gana', AI.name(), yourScore, '-', AIscore)
    elif AIscore > yourScore:
        print(AI.name(), 'gana', yourName, AIscore, '-', yourScore)
    else:
        print('empate', yourName, yourScore, AI.name(), AIscore)
