
# Projeto de jogo para treinar
# Jogo ainda em andamento

from random import randint
from time import sleep

print('-_-_' * 10 + ' Jogo dos dados ' + '-_-_' * 10)
jogar = str(input('\nBem vindo ao JOGO DOS DADOS!\n'
      'A regra é simples, o computador lançará dois dados e você tem que descobrir a soma deles.\n'
      'Cada vez que perder, a sua vida irá diminuir.\n'
      'Caso ganhe, a do computador diminui.'
      'Vamos jogar? \033[;32m[S]\033[m \033[;31m[N]\033[m\n'
      'Bora? ')[0]).split()

vjogador = 5
vcomp = 5

if (jogar[0] == 'S' or jogar[0] == 's'):
      while (jogar[0] == 'S' or jogar[0] == 's'):
            while (0 < vcomp <= 5 or 0 < vjogador <= 5):
                  print('C -> {}               J -> {}'.format(vcomp, vjogador))
                  computador = randint(2, 12)
                  sleep(0.8)
                  escolha = int(input('Faça sua escolha: '))
                  sleep(0.8)
                  print('Hora dos dados...')
                  sleep(0.8)
                  print('Você escolher {} e o ao jogar o computador tirou {}.'.format(escolha, computador))
                  if (computador != escolha):
                        vjogador = vjogador - 1
                  elif (computador == escolha):
                        vcomp = vcomp - 1
                  sleep(0.8)

                  if (vcomp == 0):
                        print('Você GANHOU!')
                        break
                  elif (vjogador == 0):
                        print('Você PERDEU!')
                        break
            jogar = str(input('Jogar novamente? \033[;32m[S]\033[m \033[;31m[N]\033[m')[0]).split()
            break
      print('Fim de jogo!')

elif (jogar[0] == 'N' or jogar[0] == 'n'):
      print('Fim de jogo!')

else:
      print('Comando inválido!')