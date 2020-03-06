def Verifica_Resultado (jogador,maquina):
    # resultado = ('Venceu','Perdeu','Empatou')
    if maquina==0: #Pedra
        if jogador==0: #Pedra
            resultado = 2 #Empatou
        elif jogador==1: #Papel
            resultado = 0 #Venceu
        elif jogador==2: #Tesoura
            resultado = 1 #Perdeu
        else:
            print('Você escolheu uma opção inválida!')
    elif maquina==1: #Papel
        if jogador==0: #Pedra
            resultado = 1 #Perdeu
        elif jogador==1: #Papel
            resultado = 2 #Empatou
        elif jogador==2: #Tesoura
            resultado = 0 #Venceu
        else:
            print('Você escolheu uma opção inválida!')
    elif maquina==2: #Tesoura
        if jogador==0: #Pedra
            resultado = 0 #Venceu
        elif jogador==1: #Papel
            resultado = 1 #Perdeu
        elif jogador==2: #Tesoura
            resultado = 2 #Empatou
        else:
            print('Você escolheu uma opção inválida!')
    return resultado
from random import randint
jogo = ('mqxjg','mqxmq','jgxjg')
op = ('Pedra', 'Papel', 'Tesoura' )
print('Escolha uma opção para jogar:\n[ 0 ] Maquina x Jogador\n[ 1 ] Maquina x Maquina\n[ 2 ] Jogador x Jogador\n')
jogo = int(input('Qual sua opção ? '))
if jogo == 0: # Máquina x Jogador
    maquina = randint(0,2)
    print('Escolha uma opção abaixo:\n[ 0 ] Pedra\n[ 1 ] Papel\n[ 2 ] Tesoura\n')
    jogador = int(input('Qual sua opção ? '))
    print('Computador jogou {}'.format(op[maquina]))
    print('Você jogou {}'.format(op[jogador]))
    print('x' * 25)
    Verifica_Resultado(jogador,maquina)
    if resultado==0:
        print('Parabéns, você venceu')
    elif resultado==1:
        print('Você perdeu')
    else:
        print('Empatou')
    print('x' * 25)
elif jogo == 1: # Máquina x Máquina
    maquina = randint(0,2)
    jogador = randint(0,2)
    print('O Computador 1 jogou {}'.format(op[maquina]))
    print('O Computador 2 jogou {}'.format(op[jogador]))
    print('x' * 25)
    Verifica_Resultado(jogador,maquina)
    if resultado==0:
        print('O computador 2 venceu')
    elif resultado==1:
        print('O computador 1 venceu')
    else:
        print('Empatou')
    print('x' * 25)
elif jogo == 2: # Jogador x Jogador
    print('Jogador 1')
    print('Escolha uma opção abaixo:\n[ 0 ] Pedra\n[ 1 ] Papel\n[ 2 ] Tesoura\n')
    maquina = int(input('Qual sua opção ? '))
    print('Jogador 2')
    print('Escolha uma opção abaixo:\n[ 0 ] Pedra\n[ 1 ] Papel\n[ 2 ] Tesoura\n')
    jogador = int(input('Qual sua opção ? '))
    print('O Jogador 1 jogou {}'.format(op[maquina]))
    print('O Jogador 2 jogou {}'.format(op[jogador]))
    print('x' * 25)
    Verifica_Resultado(jogador,maquina)
    if resultado==0:
        print('O jogador 2 venceu')
    elif resultado==1:
        print('O jogador 1 venceu')
    else:
        print('Empatou')
    print('x' * 25)
else:
    print('Você escolheu uma opção inválida para jogar')