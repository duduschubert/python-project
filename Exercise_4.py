# Exercício - sistema de perguntas e respostas
acertos = 0

print(5*'-'+ 'PERGUNTAS E RESPOSTAS'+ 5*'-' )

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

for pergunta in perguntas:    
    print('Pergunta ->', pergunta['Pergunta'])
  
    opcoes = pergunta['Opções']
    resposta = pergunta['Resposta']
    qtd_opcoes = len(opcoes)

    for i, alternativas in enumerate(opcoes):
        print(i,'-', alternativas)
    print()

    escolha = input('Escolha sua resposta: ')

    
    acertou = False
    escolha_usuario = None


    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == resposta:
                acertou = True
                

    if acertou:
        acertos += 1
        print('Você acertou ✔')
    else:
        print('Você errou ❌')
        

print(f'Você acertou {acertos}')
print('de', len(perguntas), 'perguntas!')
