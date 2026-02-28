# EXERCISE 1

def multiplicacao(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = multiplicacao(2)
triplicar = multiplicacao(3)
quadruplicar = multiplicacao(4)

print(duplicar(4))
print(triplicar(4))
print(quadruplicar(4))