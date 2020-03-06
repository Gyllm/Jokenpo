def Verifica_Resultado (jogador,maquina):
    if maquina==0: #Pedra
        if jogador==0: #Pedra
            print('Empatou')
        elif jogador==1: #Papel
            print('Você venceu')
        elif jogador==2: #Tesoura
            print('Você perdeu')
        else:
            print('Você escolheu uma opção inválida!')
    elif maquina==1: #Papel
        if jogador==0: #Pedra
            print('Você perdeu')
        elif jogador==1: #Papel
            print('Empatou')
        elif jogador==2: #Tesoura
            print('Você venceu')
        else:
            print('Você escolheu uma opção inválida!')
    elif maquina==2: #Tesoura
        if jogador==0: #Pedra
            print('Você venceu')
        elif jogador==1: #Papel
            print('Você perdeu')
        elif jogador==2: #Tesoura
            print('Empatou')
        else:
            print('Você escolheu uma opção inválida!')
from random import randint
op = ('Pedra', 'Papel', 'Tesoura' )
maquina = randint(0,2)
print('Escolha uma opção abaixo:\n[ 0 ] Pedra\n[ 1 ] Papel\n[ 2 ] Tesoura\n')
jogador = int(input('Qual sua opção ? '))
print('Computador jogou {}'.format(op[maquina]))
print('Você jogou {}'.format(op[jogador]))
print('x' * 25)
Verifica_Resultado(jogador,maquina)
print('x' * 25)