print("*********************************")
print("Bem vindo no jogo de Adivinhacao!")
print("*********************************")

numero_secreto = 7
total_de_tentativas = 3
rodada = 1

for rodada in range(1, total_de_tentativas +1):
    print("Tentativa {} de {}".format( rodada, total_de_tentativas))
    chute_str = input("Digite o seu numero: ")
    print("Voce digitou ", chute_str)
    chute = int(chute_str)

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Voce acertou!")
    else:
        if(maior):
            print("Voce errou! O numero secreto é menor.")
        elif(menor):
            print("Voce errou! O numero secreto é maior.")

    rodada = rodada + 1

print("Fim do jogo")