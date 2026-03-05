contador = 1
lista = []
# Maior número
# Menor número
# Média
# Quantidade de números pares

while contador <= 10:
    entrada = input(f'Digite {contador} numero: ')
    entrada_nova = int(entrada)
    contador += 1
    lista.append(entrada_nova)


def media():
    soma = 0
    for numero in lista:
        soma += numero
    return soma / len(lista)

def menor():
    return min(lista)

def maior():
    return max(lista)

def pares():
    pares = []
    for numero in lista:
        if numero % 2 == 0:
            pares.append
    print(pares)

maior_numero = maior()
menor_numero = menor()
media_numeros = media()     
print(f'O maior numero é {maior_numero}, o menor numero é {menor_numero} e a média é {media_numeros}')


