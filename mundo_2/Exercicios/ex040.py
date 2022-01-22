# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

nome = str(input('Qual o nome do(a) aluno(a)? '))
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))
media = (n1 + n2 + n3 + n4) / 4

if (media < 5.0):
    print('O(a) alundo(a) {} teve a média {:.2f} e ficou abaixo de 5.0. Estado: \033[;;41mREPROVADO!\033[m' .format(nome, media))
elif (media >= 5.0 and media <= 6.9):
    print('O(a) alundo(a) {} teve a média {:.2f} e ficou entre de 5.0 e 6.9. Estado: \033[;;43mRECUPERAÇÃO!\033[m' .format(nome, media))
elif (7.0 <= media <= 10):
    print('O(a) alundo(a) {} teve a média {:.2f} e ficou acima de 7.0. Estado: \033[;;42mAPROVADO!\033[m' .format(nome, media))
else:
    print('Calculo da média inválida. Tente novamente!')