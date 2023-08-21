def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_","_","_","_","_","_"]
    vidas = 5

    enforcou = False
    acertou = False

    print(letras_acertadas)

    while (not acertou and not enforcou):

        chute = input("Qual letra? ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if (chute.upper() == letra.upper()):
                print("Encontrei a letra {} na posição {}".format(letra, index))
                letras_acertadas[index] = letra
            index = index + 1

        if (not letras_acertadas.count("_")):
            acertou = True
        else:
            vidas = vidas - 1

        if (vidas == 0):
            enforcou = True

        print(letras_acertadas)

    print("Fim do jogo")


if(__name__ == "__main__"):
    jogar()
