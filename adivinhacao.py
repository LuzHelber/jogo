print("*********************************")
print("Bem vindo no jogo de Adivinhacao!")
print("*********************************")

numero_sercreto = 42

chute_str = input("Digite o seu numero: ")

print("Voce digitou ", chute_str)

chute = int(chute_str)

if(numero_sercreto == chute):
    print("Voce acertou!")
else:
    print("Voce errou!")

print("Fim do jogo")