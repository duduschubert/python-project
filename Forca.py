#EXERCÍCIO FORCA
import os

def menu_letras():
    print(5*'-'+'FORCA'+ 5*'-')
    letra_digitada = input('Digite uma letra: ').lower()
    
    
    if not letra_digitada.isalpha():
        print('Digite apenas letras!')    
        return None
    elif len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        return None

    return letra_digitada


def atualizar_palavra(palavra_secreta, letras_acertadas):
    
    palavra_formada = ''
    
    for letra_secreta in palavra_secreta:
        
        if letra_secreta in  letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    return palavra_formada   
    
def jogo():
    palavra_secreta = 'acoplado'
    tentativas = 0
    letras_acertadas = ''

    while True:
        letra = menu_letras()

        if letra is None:
            continue  # volta pro começo se for inválido

        tentativas += 1

        if letra in palavra_secreta:
            letras_acertadas += letra

        palavra_formada = atualizar_palavra(palavra_secreta, letras_acertadas)

        print(palavra_formada)

        if palavra_formada == palavra_secreta:
            os.system('cls') 
            print('Você GANHOU!! Parabéns!!')
            print('A palavra era:', palavra_secreta.upper())
            print('Suas tentativas foram:', tentativas)
            break

jogo()
    
   
