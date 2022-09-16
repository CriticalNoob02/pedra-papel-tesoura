from functions import JogadorPC, Jogador1,NomeOponente,Verificação,MostrarResult,coresTerminal
import os

os.system("cls")
ini,fim = coresTerminal(1,3,0)

## Apresentação e entrada do Nome;
print("")
print (f"{ini}########### Bem-Vindo ao Jogo Pedra, Papel e Tesoura ###########{fim}")
nome = input("Digite seu nome: ")
print(" ")

## Entrada Do Nivel;
print("Escolha o nivel do seu Rival: \n1= João, O Sem Braço \n2= Felipe, O Dois Dedos \n3= Regina, A mulher \n4= Roberta, A Leitora de Horóscopo \n5= Claudio, O Vidente \n6= ???? \n")
nivel = int(input("Digite Aqui o valor Correspondente ao seu Rival: "))
nomeDoRival = NomeOponente(nivel)

## Placar;
ptjogador = 0
ptPC = 0

os.system("cls")

while True:

    jogada1 = Jogador1()

    jogadaPC = JogadorPC(nivel)

    resultado = Verificação(jogada1, jogadaPC)

    ## Somando Placar;
    if resultado == 1:
        ptjogador += 1
    elif resultado == 2:
        pass
    else:
        ptPC += 1

    MostrarResult(resultado, nivel, jogada1, jogadaPC, nomeDoRival)

    ## Exibindo Placar;
    print(f"{nomeDoRival} = {ptPC}")
    print(f"{nome} = {ptjogador}")
    print("")

    ## Final da Partida;
    if ptjogador == 3:
        print(f"{ini}Parabens você passou de fase!{fim}")
        break
    elif ptPC == 3:
        ini,fim = coresTerminal(1,2,0)
        print(f"{ini}Infelizmente você foi Totalmente Derrotado{fim}")
        break