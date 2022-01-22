print('========== Loja jaja ==========')
valor = float(input('Qual o valor da compra? '))
opcao = int(input('Escolha a forma de pagamento:\n'
'[1] À vista dinheiro/cheque\n'
'[2] À vista no cartão\n'
'[3] 2x no cartão\n'
'[4] 3x ou mais no cartão\n'
'Qual sua escolha? '))

if (opcao == 1):
	print('O pagamento à vista dinheiro/cheque tem 10% de desconto. O valor final é de R${}.' .format(valor - (valor * 10) / 100))
elif (opcao == 2):
	print('O pagamento à vista no cartão tem 5% de desconto. O valor final é de R${}.' .format(valor - (valor * 5) / 100))
elif (opcao == 3):
	print('O pagamento em 2x não tem desconto. O valor final é de 2x de R${}.' .format(valor / 2))
elif (opcao == 4):
	print('O pagamento em 3x ou mais no cartão irá gerar 20% juros. O valor final é de R${}.' .format(valor + (valor * 20) / 100))
else:
	print('Opção inválida. Tente outra vez!')