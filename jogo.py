from functions import JogadorPC, Jogador1,NomeOponente,Verificação,MostrarResult
import random

## Entrada Do Nivel;
print ("Bem-Vindo ao Jogo Pedra, Papel e Tesoura \n")
print("Escolha o nivel do seu Rival: \n1= João, O Sem Braço \n2= Felipe, O Dois Dedos \n3= Regina, A Menor de Idade \n4= Roberta, A Leitora de Horóscopo \n5= Claudio, O Vidente \n")
nivel = int(input("Digite Aqui o valor Correspondente ao seu Rival: "))
nomeDoRival = NomeOponente(nivel)

## Placar;
ptjogador = 0
ptPC = 0

while True:

    jogada1 = Jogador1()

    jogadaPC = JogadorPC(nivel)

    resultado = Verificação(jogada1, jogadaPC)

    MostrarResult(resultado, nivel, jogada1, jogadaPC, nomeDoRival)
    
    
