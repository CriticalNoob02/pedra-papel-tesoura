import random

def coresTerminal(Estilo,Cor,Fundo):
    match Estilo:
        case 0:
            estilo = "0" ## Padrão
        case 1:
            estilo = "1" ## Negrito
        case 2:
            estilo = "4" ## Sublinhado 
        case 3:
            estilo = "7" ## Negativo
    match Cor:
        case 0:
            cor = "37" ## Padrão
        case 1:
            cor = "30" ## Cinza
        case 2:
            cor = "31" ## Vermelho
        case 3:
            cor = "32" ## Verde
        case 4:
            cor = "33" ## Amarelo
        case 5:
            cor = "34" ## Roxo
        case 6:
            cor = "35" ## Rosa
        case 7:
            cor = "36" ## Azul
    match Fundo:
        case 0:
            fundo = "40" ## Padrão
        case 1:
            fundo = "47" ## Cinza
        case 2:
            fundo = "41" ## Vermelho
        case 3:
            fundo = "42" ## Verde
        case 4:
            fundo = "43" ## Amarelo
        case 5:
            fundo = "44" ## Roxo
        case 6:
            fundo = "45" ## Rosa
        case 7:
            fundo = "46" ## Azul
    base = "\033[0;37;40m"
    padrão = (f"\033[{estilo};{cor};{fundo}m")
    return padrão,base

def NomeOponente(nivel):
    if nivel == 1:
        nome = "João, O Sem Braço"
    elif nivel == 2:
        nome = "Felipe, O Dois Dedos"
    elif nivel == 3:
        nome = "Regina, A normal"
    elif nivel == 4:
        nome = "Roberta, A Leitora de Horóscopo"
    elif nivel == 5:
        nome = "Claudio, O Vidente"
    elif nivel == 6:
        nome = "Bolsonaro"
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
    elif nivel == 6:
        jogadapc = "Arminha!"
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
    ## POntuação e frase;
    if nivel == 1:
        if resultado == 1:
            ini,fim = coresTerminal(0,3,0)
            print("")
            print(f"Sua Jogada foi {jogada1}")
            print(f"{nomeDoRival} jogou {jogadaPC}")
            print("")
            print(f"{ini}Parabens, você derrotou o {nomeDoRival}, na verdade isso é quase sua obrigação né...{fim}")
            print("")
        elif resultado == 2:
            ini,fim = coresTerminal(0,4,0)
            print("")
            print(f"Sua Jogada foi {jogada1}")
            print(f"{nomeDoRival} jogou {jogadaPC}")
            print("")
            print(f"{ini}É, parece que você é bem azarado, conseguiu empatar com um cara que só possui uma jogada...{fim}")
            print("")
        else:
            ini,fim = coresTerminal(0,2,0)
            print("")
            print(f"Sua Jogada foi {jogada1}")
            print(f"{nomeDoRival} jogou {jogadaPC}")
            print("")
            print(f"{ini}Agora você é motivo de Piada, acabou de perder para o {nomeDoRival}{fim}")
            print("")
    elif nivel == 2:
        if resultado == 1:
            ini,fim = coresTerminal(0,3,0)
            print("")
            print(f"Sua Jogada foi {jogada1}")
            print(f"{nomeDoRival} jogou {jogadaPC}")
            print("")
            print(f"{ini}Parabens, você derrotou o {nomeDoRival}, isso já pode ser motivo de orgulho?{fim}")
            print("")
        elif resultado == 2:
            ini,fim = coresTerminal(0,4,0)
            print("")
            print(f"Sua Jogada foi {jogada1}")
            print(f"{nomeDoRival} jogou {jogadaPC}")
            print("")
            print(f"{ini}Infelizmente você empatou, não se sinta tão péssimo! {fim}")
            print("")
        else:
            ini,fim = coresTerminal(0,2,0)
            print("")
            print(f"Sua Jogada foi {jogada1}")
            print(f"{nomeDoRival} jogou {jogadaPC}")
            print("")
            print(f"{ini}A vida pode ser dura as vezes.... você foi derrotado pelo {nomeDoRival}{fim}")
            print("")
    elif nivel == 3:
        if resultado == 1:
            ini,fim = coresTerminal(0,3,0)
            print("")
            print(f"Sua Jogada foi {jogada1}")
            print(f"{nomeDoRival} jogou {jogadaPC}")
            print("")
            print(f"{ini}Parabens, você derrotou a {nomeDoRival}!!{fim}")
            print("")
        elif resultado == 2:
            ini,fim = coresTerminal(0,4,0)
            print("")
            print(f"Sua Jogada foi {jogada1}")
            print(f"{nomeDoRival} jogou {jogadaPC}")
            print("")
            print(f"{ini}Ixxi, parece que você empatou com a {nomeDoRival}{fim}")
            print("")
        else:
            ini,fim = coresTerminal(0,2,0)
            print("")
            print(f"Sua Jogada foi {jogada1}")
            print(f"{nomeDoRival} jogou {jogadaPC}")
            print("")
            print(f"{ini}É, Você Perdeu, continua tudo normal...{fim}")
            print("")
    elif nivel == 4:
        if resultado == 1:
            ini,fim = coresTerminal(0,3,0)
            print("")
            print(f"Sua Jogada foi {jogada1}")
            print(f"{nomeDoRival} jogou {jogadaPC}")
            print("")
            print(f"{ini}É meu nobre, parece que Horóscopo não passa de Piada kkkkk, Você venceu!{fim}")
            print("")
        elif resultado == 2:
            ini,fim = coresTerminal(0,4,0)
            print("")
            print(f"Sua Jogada foi {jogada1}")
            print(f"{nomeDoRival} jogou {jogadaPC}")
            print("")
            print(f"{ini}Empatou!! Não te culpo, estava escrito nas estrelas...{fim}")
            print("")
        else:
            ini,fim = coresTerminal(0,2,0)
            print("")
            print(f"Sua Jogada foi {jogada1}")
            print(f"{nomeDoRival} jogou {jogadaPC}")
            print("")
            print(f"{ini}Taporra, parece que seu seu Sol estava na casa 1, sua Lua na casa 3, Mercúrio na casa... Resumindo, VOCÊ PERDEU!{fim}")
            print("")
    elif nivel == 5:
        if resultado == 3:
            ini,fim = coresTerminal(0,2,0)
            print("")
            print(f"Sua Jogada foi {jogada1}")
            print(f"{nomeDoRival} jogou {jogadaPC}")
            print("")
            print(f"{ini}Meu Amigo... Você não consegue vencer um Vidente....{fim}")
            print("")
    elif nivel == 6:
        if resultado == 3:
            ini,fim = coresTerminal(0,2,0)
            print("")
            print(f"Sua Jogada foi {jogada1}")
            print(f"{nomeDoRival} jogou {jogadaPC}")
            print("")
            print(f"{ini}Bolsonaro Jogou Arminha e você PERDEU !!{fim}")
            print("")
            print(f"{ini} ̿̿ ̿̿ ̿̿ ̿'̿'\̵͇̿̿\з= ( ▀ ͜͞ʖ▀) =ε/̵͇̿̿/’̿’̿ ̿ ̿̿ ̿̿ ̿̿  {fim}")
            print("")