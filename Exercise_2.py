# EXERCISE 1
def multiplicacao(*args):
    total = 1 
    for numero_recebido in args:
        total *= numero_recebido
    return total 

numeros_multiplicacao = multiplicacao(3,8,10)
print(numeros_multiplicacao)   

# EXERCISE 2

def par_impar(*args):
    for numero in args:    
        if numero % 2 == 0: 
            print('Este número é par!')
        else:
            print('Este número é ímpar!')
    

par_impar(2, 3, 4, 5, 6, 8)
