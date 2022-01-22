from time import sleep
from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)
print('Opções:\n'
      '[0] PEDRA\n'
      '[1] PAPEL\n'
      '[2] TESOURA')
jog = int(input('Escolha sua jogada: '))

if (jog >= 0 and jog <= 2):
      print('JO')
      sleep(0.7)
      print('KEN')
      sleep(0.7)
      print('PÔ!')
      sleep(0.7)
      print('--==' * 6)
      print('Computador jogou {}' .format(itens[comp]))
      print('Você jogou {}' .format(itens[jog]))
      print('==--' * 6)

      if (comp == 0):
            if (jog == 0):
                  print('EMPATE!')
            elif (jog == 1):
                  print('VOCÊ VENCEU!')
            elif (jog == 2):
                  print('VOCÊ PERDEU!')
      elif (comp == 1):
            if (jog == 0):
                  print('VOCÊ PERDEU!')
            elif (jog == 1):
                  print('EMPATE!')
            elif (jog == 2):
                  print('VOCÊ VENCEU!')
      elif (comp == 2):
            if (jog == 0):
                  print('VOCÊ VENCEU!')
            elif (jog == 1):
                  print('VOCÊ PERDEU!')
            elif (jog == 2):
                  print('EMPATE!')

else:
      print('Comando inválido. Tente novamente!')