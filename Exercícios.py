#EXERCÍCIO 1

numero = input("Digite aqui um numero: ")

try:
    numero_int = int(numero)
    if numero_int % 2 == 0:
        print(f'O numero {numero_int} é par.')

    else:
        print(f'O numero {numero_int} é ímpar.') 

except ValueError:
    print('Número não é inteiro, digite novamente.')        



#EXERCÍCIO 2

hora = input('Digite a hora de agora em números inteiros: ')

try:
    hora_inteira = int(hora)

    if hora_inteira in range (0,11):
        print('Bom dia.')
    
    elif hora_inteira in range (12,18):
        print('Boa tarde.')
    
    elif hora_inteira in range (18,23):
        print('Boa noite.')

    else:
        print('Hora inexistente')

except ValueError:
    print('Por favor, digite apenas números inteiros.')


#EXERCÍCIO 3

nome = input('Digite seu nome: ')
nome_curto = len(nome) <= 4
nome_normal = len(nome) in range (5,7)
nome_longo = len(nome) > 6

if nome_curto:
    print('Seu nome é curto!')

elif nome_normal:
    print('Seu nome é normal!')

elif nome_longo:
    print('Seu nome é longo!')

else:
    print('Por favor, digite apenas letras.')

