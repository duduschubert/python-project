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
            numero_float = float(numero)
            numero_dois_float = float(numero_dois)
           
            print('Realizando o cálculo...')   
            
            if operacao == 1:
                print(f'{numero_float} + {numero_dois_float} =', numero_float + numero_dois_float)
                                        
            elif operacao == 2:
                print(f'{numero_float} - {numero_dois_float} =', numero_float - numero_dois_float) 
                                
            elif operacao == 3:
                print(f'{numero_float} * {numero_dois_float} =', numero_float * numero_dois_float)

            elif operacao == 4:
                try:
                    print(f'{numero_float} / {numero_dois_float} =', numero_float / numero_dois_float)
                           
                except ZeroDivisionError:
                    print('Divisão por zero é impossível')
                    continue        
           
            elif operacao == 5:
                print(f'{numero_float} ** {numero_dois_float} =', numero_float ** numero_dois_float)
                
                        
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


