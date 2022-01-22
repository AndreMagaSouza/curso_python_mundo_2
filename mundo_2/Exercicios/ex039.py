# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
sexo = str(input('Qual o seu sexo? [M] ou [F]: ')).strip()

if (sexo == 'M' or sexo == 'm'):
    ano = int(input('Ano de nascimento: '))
    atual = date.today().year
    idade = atual - ano
    if (idade == 18):
        print('Estamos em {}. Você nasceu em {} e tem {} anos.\n'
              'Você precisa se alistar neste ano!' .format(atual, ano, idade))
    elif (idade > 18):
        print('Estamos em {}. Você nasceu em {} e tem {} anos.\n'
              'O seu alistamento foi há {} anos.' .format(atual, ano, idade, (idade - 18)))
    else:
        print('Estamos em {}. Você nasceu em {} e tem {} anos.\n'
              'Seu alistamento será em {} anos, em {}.'.format(atual, ano, idade, (18 - idade), (atual + (18 - idade))))

elif (sexo == 'F' or sexo == 'f'):
    print('Você é uma mulher. Não precisa se alistar.\n'
          'Tenha um ótimo dia!')
else:
    print('Comando inválido. Tente novamente!')