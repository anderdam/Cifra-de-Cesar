#  Alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
#               'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
#               'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#  Converter o texto em código ASCII e guardar os códigos na lista:


#  def decrypt(texto_original, key):


def encriptar(mensagem_original, chave):
    cifra = ''

    for i in range(len(mensagem_original)):
        char = mensagem_original[i]

        if char.isupper():
            cifra += chr((ord(char) + chave - 65) % 26 + 65)
        else:
            cifra += chr((ord(char) + chave - 97) % 26 + 97)
    return cifra


def descriptografar(mensagem_original, chave):
    cifra = ''

    for i in range(len(mensagem_original)):
        char = mensagem_original[i]

        if char.isupper():
            cifra += chr((ord(char) - chave - 65) % 26 + 65)
        else:
            cifra += chr((ord(char) - chave - 97) % 26 + 97)
    return cifra


mensagem_original = input("Digite o texto que será codificado ou decodificado: ")
chave = int(input("Digite o valor que será utilizado como chave (1 a 26): "))
modo = int(input("O que você deseja fazer, codificar [1] ou decodificar [2]? "))

if modo == 1:
    print(f'A mensagem cifrada é: {encriptar(mensagem_original, chave)}')
elif modo == 2:
    print(f'A mensagem cifrada é: {descriptografar(mensagem_original, chave)}')





