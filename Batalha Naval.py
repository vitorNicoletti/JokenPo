import random
#navios jogador
mapaNJ = [[' ']]
mapaNC = [[' ']]
mapaJ = [[' ']]
mapaC = [[' ']]
indice = [[' ']]
for i in range(1,11):
    mapaNJ[0].append(f'{i}')
    mapaNC[0].append(f'{i}')
    mapaJ[0].append(f'{i}')
    mapaC[0].append(f'{i}')




for i in range(6):
    mapaNJ.append([f'{i+1}','-', '-','-','-','-','-','-','-','-','-'])
    mapaNC.append([f'{i+1}','-','-','-','-','-','-','-','-','-','-'])
    mapaJ.append([f'{i+1}','-','-','-','-','-','-','-','-','-','-'])
    mapaC.append([f'{i+1}','-','-','-','-','-','-','-','-','-','-'])
    print('  '.join(mapaC[i]))




for i in range(5):
    linha=int(input(f'Defina a linha do {i+1} navio: '))
    coluna=int(input(f'Defina a coluna do {i+1} navio: '))
   
    while (linha<1) or (linha>5) or (coluna<1) or (coluna>10) or (mapaNJ[linha][coluna]) == 'O':
        print('ERRO:Posição inválida')
        linha=int(input(f'Defina a linha do {i+1} navio: '))
        coluna=int(input(f'Defina a coluna do {i+1} navio: '))
    
    mapaNJ[linha][coluna] = 'O'
    ####
    linhaPC = random.randint(1,5)
    colunaPC = random.randint(1,10)

    while mapaNC[linhaPC][colunaPC] == 'O':
        linhaPC = random.randint(1,5)
        colunaPC = random.randint(1,10)

    mapaNC[linhaPC][colunaPC] = 'O'


    for i in range(6):
        print('  '.join(mapaNJ[i]))

pontosJ = 0
pontosC = 0
while True:

    print('\nTabuleiro de Jogadas\nSuas Jogadas:')
    for i in range(6):
        print('  '.join(mapaJ[i]))
    print('Computador:')
    for i in range(6):
        print('  '.join(mapaC[i]))
    print('')


    linha=int(input('Defina a linha da tentativa: '))
    coluna=int(input('Defina a coluna da tentativa: '))
   
    while (linha<1) or (linha>5) or (coluna<1) or (coluna>10) or (mapaNJ[linha][coluna]) == 'X':
        print('ERRO:Posição inválida')
        linha=int(input('Defina a linha da tentativa: '))
        coluna=int(input('Defina a coluna da tentativa: '))
    print(mapaNC[linha][coluna])

    if mapaNC[linha][coluna] == 'O':
        mapaJ[linha][coluna] = 'O'
        pontosJ += 1
    else:
        mapaJ[linha][coluna] = 'X'

    if pontosJ == 5:
        print("Jogador 1 Vence!")
        break

    
    linhaPC = random.randint(1,5)
    colunaPC = random.randint(1,10)

    while mapaC[linhaPC][colunaPC] == 'O' or mapaC[linhaPC][colunaPC] == 'X':
        linhaPC = random.randint(1,5)
        colunaPC = random.randint(1,10)

    if mapaNJ[linhaPC][colunaPC] == 'O':
        mapaC[linhaPC][colunaPC] = 'O'
        pontosC += 1
    else:
        mapaC[linhaPC][colunaPC] = 'X'

    if pontosC == 5:
        print("Computador Vence!")
        break
for i in range(6):
    print('  '.join(mapaNC[i]))