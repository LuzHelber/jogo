import random

print("*********************************")
print("Bem vindo no jogo de Adivinhacao!")
print("*********************************")

numero_secreto = random.randrange(1,50)
total_de_tentativas = 3

for rodada in range(1, total_de_tentativas +1):
    print("Tentativa {} de {}".format( rodada, total_de_tentativas))
    chute_str = input("Digite um numero entre 1 e 50: ")
    print("Voce digitou ", chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 50):
        print("Voce deve digitar um numero entre 1 e 50!")
        continue

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Voce acertou!")
        break
    else:
        if(maior):
            print("Voce errou! O numero secreto é menor.")
        elif(menor):
            print("Voce errou! O numero secreto é maior.")

print("Fim do jogo")