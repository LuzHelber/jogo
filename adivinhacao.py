print("*********************************")
print("Bem vindo no jogo de Adivinhacao!")
print("*********************************")

numero_secreto = 42

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
        print("Voce errou! O numero é secreto menor.")
    elif(menor):
        print("Voce errou! O numero é secreto maior.")

print("Fim do jogo")