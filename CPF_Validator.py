cpf = '74682489070'
nove_digitos = cpf[:9]

contador = 10
resultado = 0

for numero in nove_digitos:
    resultado += (int(numero) * contador) 
    contador -= 1

digito_1 = (resultado * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_cpf = nove_digitos + str(digito_1)

contador2 = 11
resultado2 = 0

for numero in dez_cpf:
    resultado2 += (int(numero) * contador2) 
    contador2 -= 1

digito_2 = (resultado2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

print(digito_1)
print(digito_2)

novo_cpf = f'{nove_digitos}{digito_1}{digito_2}'

if cpf == novo_cpf:
    print('Seu CPF é válido')

else:
    print('CPF inválido')