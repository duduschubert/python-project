import os

lista_de_compra = []

while True:
    print('FAÇA SUA LISTA DE COMPRA')
    print('Selecione uma opção')
    menu = input('[i]nserir [r]emover [l]istar: ')

    if not menu.isalpha():
        print('Digite apenas i, a ou l')
        continue
    if len(menu) > 1:
        print('Digite apenas UMA letra') 
        continue       

 
    if menu == 'i':
        os.system('cls')
        item = input('Digite o item a adicionar: ').upper()
        lista_de_compra.append(item)
        print(f'{item} adicionado com sucesso!\n')

        
    elif menu == 'r':
        os.system('cls')
        print('\nItens da lista')

        indice_str = input('Qual índice deseja remover: ')
        
        try:
            indice = int(indice_str)
            del lista_de_compra[indice]   
            print(f'{indice, item} removido com sucesso!\n')
        
        except IndexError:
            print('Não foi possível apagar esse índice')
        except ValueError:
            print('Digite um numero inteiro.') 
        except Exception:
            print('Erro desconhecido!')
        
    elif menu == 'l':
        os.system('cls')

        if len(lista_de_compra) == 0:
            print('Lista vazia!')

        print('\nItens da lista')
        for i, item, in enumerate(lista_de_compra):
            print(f'{i, item}')

    else:   
        break
   

    
    






    