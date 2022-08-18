import random

def NomeOponente(nivel):
    if nivel == 1:
        nome = "João, O Sem Braço"
    elif nivel == 2:
        nome = "Felipe, O Dois Dedos"
    elif nivel == 3:
        nome = "Regina, A Menor de Idade"
    elif nivel == 4:
        nome = "Roberta, A Leitora de Horóscopo"
    elif nivel == 5:
        nome = "Claudio, O Vidente"
    return nome

def Jogador1():
    ## Entrada de Dados;
    print("1 = Pedra;")
    print("2 = Papel;")
    print("3 = Tesoura;")
    jogada = int(input("Digite sua Jogada:"))

    ## Decisão;
    if jogada == 1:
        jogada = "Pedra"
    elif jogada == 2:
        jogada = "Papel"
    elif jogada == 3:
        jogada = "Tesoura"
    else:
        print("Comando Inválido, por favor Digite Novamente! ")
        Jogador1()
    return jogada

def JogadorPC(nivel):
    ## Puxando Jogadas;
    global jogada1

    ## Escalando Niveis de Dificuldade;
    if nivel == 1:
        jogadapc = "Pedra"
    if nivel == 2:
        jogadapc = random.choice(["Papel","Tesoura"])
    elif nivel == 3:
        jogadapc = random.choice(["Pedra","Papel","Tesoura"])
    elif nivel == 4:
        if jogada1 == "Pedra":
            jogadapc = random.choice(["Papel", "Tesoura"])
        elif jogada1 == "Papel":
            jogadapc = random.choice(["Pedra", "Tesoura"])
        if jogada1 == "Tesoura":
            jogadapc = random.choice(["Papel", "Pedra"])
    elif nivel == 5:
        if jogada1 == "Pedra":
            jogadapc = "Papel"
        elif jogada1 == "Papel":
            jogadapc = "Tesoura"
        if jogada1 == "Tesoura":
            jogadapc = "Pedra"
    return jogadapc

def Verificação(jogada1, jogadaPC):
    
    ## Vitória;
    if (jogada1 == "Pedra" and jogadaPC == "Tesoura") or (jogada1 == "Papel" and jogadaPC == "Pedra") or (jogada1 == "Tesoura" and jogadaPC == "Papel"):
        resultado = 1
    ## Empate;
    elif jogada1 == jogadaPC:
        resultado = 2
    ## Derrota;
    else:
        resultado = 3
    return resultado

def MostrarResult(resultado, nivel, jogada1, jogadaPC, nomeDoRival):
    global ptjogador
    global ptPC

    if nivel == 1:
        if resultado == 1:
            ptjogador += 1
            print("")
            print(f"Sua Jogada foi {jogada1}")
            print(f"{nomeDoRival} jogou {jogadaPC}")
            print("")
            print(f"Parabens, você derrotou o {nomeDoRival}, na verdade isso é quase sua obrigação né...")
            print("")
        elif resultado == 2:
            print("")
            print(f"Sua Jogada foi {jogada1}")
            print(f"{nomeDoRival} jogou {jogadaPC}")
            print("")
            print(f"É, parece que você é bem azarado, conseguiu empatar com um cara que só possui uma jogada...")
            print("")
        else:
            ptPC += 1
            print("")
            print(f"Sua Jogada foi {jogada1}")
            print(f"{nomeDoRival} jogou {jogadaPC}")
            print("")
            print(f"Agora você é motivo de Piada, acabou de perder para o {nomeDoRival}")
            print("")
    elif nivel == 2:
        pass