casa = float(input('Valor da casa: '))
sal = float(input('Qual seu salário: '))
fin = int(input('Quantos anos de financiamento: '))

temp = fin * 12
parc = casa / temp
lim = (sal * 30) / 100

print('Para pagar uma casa no valor de R${:.2f} em {} anos, o empréstimo será de R${:.2f}.' .format(casa, fin, parc))

if (parc > lim):
	print('\033[0;31mNEGADO!\033[m')
else:
    print('\033[0;32mAprovado!\033[m')
