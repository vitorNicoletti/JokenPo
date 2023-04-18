#1-pedra 2-papel 3-tesoura.

#definir as variaveis da tabela de pontos
pontos1=0
pontos2=0
#criando as funcoes do jogo 

#as funcoes foram criadas principalmente pois a repeticao do codigo ia ficar
#muito extensa. Entretanto, algumas partes do codigo ainda se repetem, porem,
#com menos linhas repetidas.

#so para nao ter q reescrever todo o texto, funcao de print do fim do jogo.
def fimdejogo():
    print(f'\ntabela de pontos\n------\n{pontos1} x {pontos2}\n')
    print(  'obrigado por jogar!\nJogo feito por:\n'
        'Vitor Nicoletti\n'
        'Vinícios Yamamoto Borges\n'
        'Gabriel Vidal Schneider\n'
        'Luca  Dias David\n'
        'Mohamad Kassem Diab')
#os "returns" sao utilizados para sabermos quem ganhou a partida,
#o jogador 1 ou o jogador 2, ex: quando retorna 1, vitoria para o 1             
def jokenpo(jogada1,jogada2):
    #checa se nao foi empate, depois disso, checa todas as possibilidades,
    #aproveitando para printar quem ganhou.
    if(jogada1==jogada2):
        print ('\n empate\n')
    elif(jogada1 == 1):
        if(jogada2==3):
            print('\npedra x tesoura \n\npedra vence!\n')
            return(1)
        else:
            print('\npedra x papel \n\npapel vence!\n')
            return (2)

    elif(jogada1==2):
        if(jogada2==1):
            print('\npapel x pedra\n\npapel vence\n')
            return(1)
        else:
            print('\npapel x tesoura \n\ntesoura ganha\n')
            return(2)

    elif(jogada1==3):
        if(jogada2==1):
            print('\ntesoura x pedra \n\npedra ganha\n')
            return(2)
        else:
            print('\ntesoura x papel \n\ntesoura ganha\n')
            return(1)
            
#pergunta o modo de jogo
modo = int(input('--JOKENPO--\ndefina o modo de jogo:\n1-humano x humano\n2-humano x computador\n3-computador x computador\n'))
#Checagem de qual modo de jogo escolhido
if(modo==1):
    while True:

        print('escolha entre 1,2 e 3. Sendo:\n 1-pedra\n 2-papel\n 3-tesoura')
        #armazena as jogadas
        a = int(input('primeira jogada: '))
        b = int(input('segunda jogada '))
        #checagem se os numeros sao validos
        if((a<=3 and a>=1) and (b<=3 and b>=1) ):
        #checagem de quem ganhou,
        #quem vence tem +1 nos pontos da tabela, definidos por pontos1 e pontos2.
        #nao achei alguma forma de nao usar a var ganhador, pois se eu repetir 
        #a funcao dentro dos ifs, acredito que ela rode mais de uma vez.
        #o processo de distribuir os pontos sao iguais para todos os modos.
            ganhador = jokenpo(a, b)
            if (ganhador == 1):
                print('jogador 1 vence')
                pontos1 += 1
            elif (ganhador == 2):
                print('jogador 2 vence')
                pontos2 += 1 
        else:
            print('\n Valor não existente, favor rever jogadas e tentar novamente \n')
        #print da tabela de pontos
        print(f'\ntabela de pontos\n------\n{pontos1} x {pontos2}\n')
        #perguntaa se quer jogar mais
        if(int(input('digite 1 para continuar, ou qualquer outro numero para sair.\n R:')) != 1):
           fimdejogo()
           break
elif(modo==2):

    import random

    while True:
        print('escolha entre 1,2 e 3. Sendo:\n 1-pedra\n 2-papel\n 3-tesoura\n')
        #armazena a jogada
        a = int(input('sua jogada: '))
        #checa se o valor de a existe e roda ou nao o codigo
        if(a>=1 and a<=3):
            ganhador = jokenpo(a, random.randint(1,3))
            if(ganhador==1):
                print('jogador 1 vence')
                pontos1 += 1
            elif(ganhador==2):
                print('jogador 2 vence')
                pontos2 += 1

        else:
            print('Valor não existente, favor rever jogadas e tentar novamente')
    
        print(f'\ntabela de pontos\n------\n{pontos1} x {pontos2} \n')

        if(int(input('digite 1 para continuar, ou qualquer outro numero para sair.\n R:')) != 1):
            fimdejogo()
            break
elif(modo==3):
    
    import random

    while True:
        ganhador = jokenpo(random.randint(1,3), random.randint(1,3))
        if(ganhador == 1):
            print('jogador 1 vence')
            pontos1 += 1
        elif(ganhador == 2):
            print('jogador 2 vence')
            pontos2 += 1

        print(f'\ntabela de pontos\n------\n{pontos1} x {pontos2} \n')

        if(int(input('digite 1 para continuar, ou qualquer outro numero para sair.\n R:')) != 1):
            fimdejogo()
            break
