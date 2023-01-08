from colorama import Fore, Back
from random import randint
opcoes = {
    '1': '1',
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9'
}
jogadores = ['jogador1', 'jogador2']
vez = None


def criar_tabuleiro(tabuleiro):
    print('-------------')
    print(f"| {tabuleiro['1']} | {tabuleiro['2']} | {tabuleiro['3']} |")
    print('-------------')
    print(f"| {tabuleiro['4']} | {tabuleiro['5']} | {tabuleiro['6']} |")
    print('-------------')
    print(f"| {tabuleiro['7']} | {tabuleiro['8']} | {tabuleiro['9']} |")
    print('-------------')


def ganhou_ou_nao(jogando):
    if jogando['1'] == jogando['2'] == 'X' and jogando['2'] == jogando['3']:
        return True
    elif jogando['4'] == jogando['5'] and jogando['5'] == jogando['6']:
        return True
    elif jogando['7'] == jogando['8'] and jogando['8'] == jogando['9']:
        return True
    elif jogando['1'] == jogando['4'] and jogando['4'] == jogando['7']:
        return True
    elif jogando['2'] == jogando['5'] and jogando['5'] == jogando['8']:
        return True
    elif jogando['3'] == jogando['6'] and jogando['6'] == jogando['9']:
        return True
    elif jogando['1'] == jogando['5'] and jogando['5'] == jogando['9']:
        return True
    elif jogando['3'] == jogando['5'] and jogando['5'] == jogando['7']:
        return True
    return False


def jogador(marcando, x, esc, op):
    global jogadores
    try:
       if marcando[esc] != 'X' and marcando[esc] != '0':
            marcando[esc] = op
    except KeyError:
            print('Insira um valor válido!')
    else:
        print('Escolha uma opção válida!')


def ganhou(jogador_winner):
    global opcoes
    if ganhou_ou_nao(opcoes) == True:
        print(Fore.GREEN +f'Parabens! {jogador_winner}, você ganhou!')
        criar_tabuleiro(opcoes)


def jogatina(marcado):
    quem_comeca = randint(0, 1)
    global jogadores
    global vez
    vez = 0
    print('\n\nDigam seus nomes, meu sistema computará quem vai começar! \n')
    jogadores[0] = input('Qual o nome do jogador 1? ')
    jogadores[1] = input('Qual o nome do jogador 2? ')
    if quem_comeca == 0:
        print(f'Começe, {jogadores[0]}!')
    else:
        print(f'Começe, {jogadores[1]}!')
    vez = quem_comeca
    #REDUZIR CÓDIGO
    while ganhou_ou_nao(opcoes) == False:
        if vez == 0:
            criar_tabuleiro(opcoes)
            escolha = input(Fore.BLUE + f'{jogadores[0]}, escolha entre as alternativas válidas:')
            jogador(opcoes, 0, escolha, 'X')
            ganhou(jogadores[0])
            vez = 1
        elif vez == 1:
            criar_tabuleiro(opcoes)
            escolha = input(Fore.LIGHTMAGENTA_EX + f'{jogadores[1]}, escolha entre as alternativas válidas:')
            jogador(opcoes, 1, escolha, 'O')
            jogadores[1]
            ganhou(jogadores[1])
            vez = 0



jogatina(opcoes)
