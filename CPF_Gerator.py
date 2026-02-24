
# entrada = input('Digite aqui seu CPF: ')
# cpf = re.sub(
#     r'[^0-9]',
#     '',
#     entrada
#     )
# entrada_sequencia = entrada == entrada[0] * len(entrada)

# if entrada_sequencia:
#     print('Você enviou dados sequenciais.')
#     sys.exit()

import re
import sys
import random

for _ in range(100):

    nove_digitos = ''

    for i in range(9):
        nove_digitos += str(random.randint(0, 9))

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
        resultado2 += int(numero) * contador2
        contador2 -= 1

    digito_2 = (resultado2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0


    cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'

    print(cpf_gerado)