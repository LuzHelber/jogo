import random

print("*********************************")
print("Bem vindo no jogo de Adivinhacao!")
print("*********************************")

numero_secreto = random.randrange(1,51)
total_de_tentativas = 0

print("Qual o nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Defina o nível: "))

if (nivel == 1):
    total_de_tentativas = 20
elif (nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

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