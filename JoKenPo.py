def Verifica_Resultado (jogador,maquina):
    # x = ('Venceu','Perdeu','Empatou')
    if maquina==0: #Pedra
        if jogador==0: #Pedra
            x=2 #Empatou
        elif jogador==1: #Papel
            x=0 #Venceu
        elif jogador==2: #Tesoura
            x=1 #Perdeu
        else:
            print('Você escolheu uma opção inválida!')
    elif maquina==1: #Papel
        if jogador==0: #Pedra
            x=1 #Perdeu
        elif jogador==1: #Papel
            x=2 #Empatou
        elif jogador==2: #Tesoura
            x=0 #Venceu
        else:
            print('Você escolheu uma opção inválida!')
    elif maquina==2: #Tesoura
        if jogador==0: #Pedra
            x=0 #Venceu
        elif jogador==1: #Papel
            x=1 #Perdeu
        elif jogador==2: #Tesoura
            x=2 #Empatou
        else:
            print('Você escolheu uma opção inválida!')
    return x


from random import randint
import getpass
op = ('Pedra', 'Papel', 'Tesoura')
jogo=1
while jogo !=0:
    print('MODO DE JOGO:\n[1] Maquina x Jogador\n[2] Maquina x Maquina\n[3] Jogador x Jogador\n[0] Sair do Jogo\n')
    jogo = int(input('Qual sua opção ? '))
    if jogo == 1: # Máquina x Jogador
        maquina = randint(0,2)
        jogador=0
        while jogador !=3:
            print('\nEscolha uma opção abaixo:\n[0] Pedra\n[1] Papel\n[2] Tesoura\n[3] Retornar ao menu anterior\n')
            jogador = int(input('Qual sua opção ? '))
            if jogador<3:
                print('x' * 25)
                print('Computador jogou {}'.format(op[maquina]))
                print('Você jogou {}'.format(op[jogador]))
                print('x' * 25)
                resultado=Verifica_Resultado(jogador,maquina)    
                if resultado==0:
                    print('Parabéns, você venceu')
                elif resultado==1:
                    print('Você perdeu')
                else:
                    print('Empatou')
            else:
                print('x' * 25)
                print('Escolha uma opção válida para jogar')
            print('x' * 25)
    elif jogo == 2: # Máquina x Máquina
        maquina = randint(0,2)
        jogador = randint(0,2)
        print('x' * 25)
        print('O Computador 1 jogou {}'.format(op[maquina]))
        print('O Computador 2 jogou {}'.format(op[jogador]))
        print('x' * 25)
        resultado= Verifica_Resultado(jogador,maquina)
        if resultado==0:
            print('O computador 2 venceu')
        elif resultado==1:
            print('O computador 1 venceu')
        else:
            print('Empatou')
        print('x' * 25)
    elif jogo == 3: # Jogador x Jogador
        print('x' * 25)
        print('JOGADOR 1')
        print('\nEscolha uma opção abaixo:\n[0] Pedra\n[1] Papel\n[2] Tesoura\n')
        maquina = int(getpass.getpass('Qual sua opção ? '))
        if maquina<=2:
            print('x' * 25)
            print('JOGADOR 2')
            print('\nEscolha uma opção abaixo:\n[0] Pedra\n[1] Papel\n[2] Tesoura\n')
            jogador = int(getpass.getpass('Qual sua opção ? '))
            if jogador<=2:
                print('x' * 25)
                print('O Jogador 1 jogou {}'.format(op[maquina]))
                print('O Jogador 2 jogou {}'.format(op[jogador]))
                print('x' * 25)
                resultado=Verifica_Resultado(jogador,maquina)
                if resultado==0:
                    print('O jogador 2 venceu')
                elif resultado==1:
                    print('O jogador 1 venceu')
                else:
                    print('Empatou')
            else:
                print('x' * 25)
                print('Escolha uma opção válida para jogar')
            print('x' * 25)
            print('\n')
        else:
            print('x' * 25)
            print('Escolha uma opção válida para jogar')
            print('x' * 25)
    elif jogo==0:
        print('Saindo do jogo')
        quit
    else:
        print('x' * 25)
        print('Escolha uma opção válida para jogar')