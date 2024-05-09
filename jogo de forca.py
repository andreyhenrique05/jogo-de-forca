

def escolher_palavra():
    palavras = ['python', 'programacao', 'computador', 'teclado', 'mouse', 'jogo']
    return random.choice(palavras)

def mostrar_palavra(palavra, letras_corretas):
    resultado = ''
    for letra in palavra:
        if letra in letras_corretas:
            resultado += letra
        else:
            resultado += '_'
    return resultado

def jogar_forca():
    palavra = escolher_palavra()
    letras_corretas = []
    tentativas_restantes = 6
    while tentativas_restantes > 0:
        print("\nPalavra: ", mostrar_palavra(palavra, letras_corretas))
        tentativa = input("Digite uma letra: ").lower()
        if tentativa in palavra:
            letras_corretas.append(tentativa)
            print("Letra correta!")
        else:
            tentativas_restantes -= 1
            print("Letra incorreta! Você tem {} tentativas restantes.".format(tentativas_restantes))
        if mostrar_palavra(palavra, letras_corretas) == palavra:
            print("\nParabéns! Você venceu!")
            break
    else:
        print("\nGame Over! A palavra era:", palavra)

jogar_forca()
