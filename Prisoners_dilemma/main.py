# Translation of the Code created by Sanjin Dedic creator of Robotix.com.au
# Class Game theory - Ph.D in Economics UAM
# Confesar o Mentir

import AIsimulation, AhumanGame, SiempreConfesar, SiempreMentir, titForTat, AleatorioBasic, ConfesarAleatorio, MentirAleatorio, \
    Resentido, pavlov, ES, myStrategy

choices = {'1-SiempreConfesar', '2-SiempreMentir', '3-titForTat', '4-AleatorioBasic', '5-ConfesarAleatorio',
           '6-MentirAleatorio', '7-Resentido', '8-pavlov', '9-ES', '10-myStrategy'}

strategies = {1: SiempreConfesar, 2: SiempreMentir, 3: titForTat, 4: AleatorioBasic, 5: ConfesarAleatorio, 6: MentirAleatorio,
              7: Resentido, 8: pavlov, 9: ES, 10: myStrategy}

print('Estas son las opciones del juego')
print('presiona 1 para probar una estrategia contra todas las demas estrategias ')
print('presiona 2 para jugar con una estrategia de tu elección ')
choice = int(input())

if choice == 1:
    print('Lista de estrategias ')
    print(choices)
    num = int(input('Escoge la estrategia por su numero '))
    strategy = strategies[num]
    AIsimulation.testStrategy(strategy, 20)

if choice == 2:
    print('Contra quien quieres jugar? ')
    print(choices)
    num = int(input('Escoga la estrategia por su numero '))
    strategy = strategies[num]
    rounds = int(input('Cuantos rounds quieres jugar?: '))
    AhumanGame.play(strategy, rounds)
