# Crie um programa que faça o computador jogar Jokenpô com você.
from time import sleep
from random import randint

comp = randint(1, 3)

print('==--==--' * 2)
print('    Jokenpô    ')
print('==--==--' * 2)
escolha = int(input('Escolha:\n'
                    '[1] PEDRA\n'
                    '[2] PAPEL\n'
                    '[3] TESOURA\n'
                    'Sua jogada: '))

if (escolha >= 1 and escolha <= 3):
    print('JO')
    sleep(0.7)
    print('KEN')
    sleep(0.7)
    print('PÔ!')
    sleep(0.7)

    if (comp == escolha):
        if (comp == 1 == escolha):
            print('==--' * 10)
            print('O computador jogou PEDRA\n'
                  'Você jogou PEDRA')
            print('==--' * 10)
            print('EMPATE!')
        elif (comp == 2 == escolha):
            print('==--' * 10)
            print('O computador jogou PAPEL\n'
                  'Você jogou PAPEL')
            print('==--' * 10)
            print('EMPATE!')
        elif (comp == 3 == escolha):
            print('==--' * 10)
            print('O computador jogou TESOURA\n'
                  'Você jogou TESOURA')
            print('==--' * 10)
            print('EMPATE!')

    elif (comp != escolha):
        if (escolha == 1 and comp == 3):
            print('==--' * 10)
            print('O computador jogou TESOURA\n'
                  'Você jogou PEDRA')
            print('==--' * 10)
            print('Você VENCEU!')
        elif (escolha == 2 and comp == 1):
            print('==--' * 10)
            print('O computador jogou PEDRA\n'
                  'Você jogou PAPEL')
            print('==--' * 10)
            print('Você VENCEU!')
        elif (escolha == 3 and comp == 2):
            print('==--' * 10)
            print('O computador jogou PAPEL\n'
                  'Você jogou TESOURA')
            print('==--' * 10)
            print('Você VENCEU!')

        if (comp == 1 and escolha == 3):
            print('==--' * 10)
            print('O computador jogou PEDRA\n'
                  'Você jogou TESOURA')
            print('==--' * 10)
            print('Você PERDEU!')
        elif (comp == 2 and escolha == 1):
            print('==--' * 10)
            print('O computador jogou PAPEL\n'
                  'Você jogou PEDRA')
            print('==--' * 10)
            print('Você PERDEU!')
        elif (comp == 3 and escolha == 2):
            print('==--' * 10)
            print('O computador jogou TESOURA\n'
                  'Você jogou PAPEL')
            print('==--' * 10)
            print('Você PERDEU!')

elif (escolha == 0 or escolha > 3):
    print('Escolha inválida. Tente novamente!')
