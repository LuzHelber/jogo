import random

def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    letras_acertadas = ["_" for letra in palavra_secreta]
    vidas = 10

    enforcou = False
    acertou = False

    print(letras_acertadas)

    while (not acertou and not enforcou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        index = 0
        for letra in palavra_secreta:
            if (chute == letra ):
                print("Encontrei a letra {} na posição {}".format(letra, index))
                letras_acertadas[index] = letra
            index +=  1

        if (not letras_acertadas.count("_")):
            acertou = True
        else:
            vidas = vidas - 1

        if (vidas == 0):
            enforcou = True

        print(letras_acertadas)

    if(acertou):
        print("Voce ganhou!!")
    else:
        print("Voce perdeu!!")
    print("Fim do jogo")


if(__name__ == "__main__"):
    jogar()
