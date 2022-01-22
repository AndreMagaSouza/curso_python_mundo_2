num = int(input('Digite um número inteiro: '))
op = int(input('Digite a opção de conversão:\n'
'[1] Binário\n'
'[2] Octal\n'
'[3] Hexadecimal\n'
'Sua opção: '))
if op == 1:
	print('O valor {} convertido apra binário é {}.' .format(num, bin(num)[:2]))
elif op == 2:
	print('O valor {} convertido apra octal é {}.' .format(num, oct(num)[:2]))
elif op == 3:
	print('O valor {} convertido apra hexadecimal é {}.' .format(num, hex(num)[:2]))
else:
	print('Valor inválido. Tente novamente!')