# CALCULADORA EXERCÍCIO
def menu():
       
        print(5*'-'+ 'CALCULADORA'+ 5*'-' )
        print(8*'-'+'MENU'+ 9*'-')
        print('1 - Adição')
        print('2 - Subtração')   
        print('3 - Multiplicação')
        print('4 - Divisão')
        print('5 - Potenciação')
        print('') 


def calculadora ():
    while True:  
        menu()  
        try: 
            operacao = int(input('Selecione a operação: '))
           
            if operacao not in [1, 2, 3, 4, 5]:
                print('Digite uma operação válida')
                continue
           
            numero = input('Digite o valor: ')
            numero_dois = input('Digite o segundo valor: ')
            numero_int = int(numero)
            numero_dois_int = int(numero_dois)
           
                
            if operacao == 1:
                resultado = numero_int + numero_dois_int
                print(f'Seu resultado foi: {resultado}')
                        
            elif operacao == 2:
                resultado = numero_int - numero_dois_int
                print(f'Seu resultado foi: {resultado}')
                
            elif operacao == 3:
                resultado = numero_int * numero_dois_int
                print(f'Seu resultado foi: {resultado}')

            elif operacao == 4:
                
                try:
                    resultado = numero_int / numero_dois_int
                    print(f'Seu resultado foi: {resultado}')
                
                except ZeroDivisionError:
                    print('Divisão por zero é impossível')
                    continue     
                
            elif operacao == 5:
                resultado = numero_int ** numero_dois_int
                print(f'Seu resultado foi: {resultado}')
                        
            else: 
                print('Operação inválida')
                break
        
        except ValueError:
            print('Operação inválida')
            continue     
        
        sair = input('Deseja encerrar? [s]im: ').lower().startswith('s')
        
        if sair is True:
            print('Encerrando programa...')
            break
        

calculadora()


