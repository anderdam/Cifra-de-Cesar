#  Alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
#               'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
#               'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#  Converter o texto em código ASCII e guardar os códigos na lista:


def encrypt(texto_orig, key):
    for letra in texto_orig:  # Converte cada letra do texto em ASCII
        codigo_ascii = [ord(letra)]
        for code in codigo_ascii:  # Pega o valor ASCII gerado e adiciona a chave para criptografar
            coded_alfabeto = [code + key]
            #  print(f'O código ASCII de {letra} é {codigo_ascii}: ')
            #  print(f'O código mudou de {code} para {coded_alfabeto}: ')
            for i in coded_alfabeto:
                new_texto = ','.join([chr(i)])
                print(f'O novo texto é  {new_texto} ')
                #  return codigo_final


def decrypt(texto_orig, key):
    for letra in texto_orig:  # Converte cada letra do texto em ASCII
        codigo_ascii = [ord(letra)]
        for code in codigo_ascii:  # Pega o valor ASCII gerado e adiciona a chave para criptografar
            coded_alfabeto = [code - key]
            #  print(f'O código ASCII de {letra} é {codigo_ascii}: ')
            #  print(f'O código mudou de {code} para {coded_alfabeto}: ')
            for i in coded_alfabeto:
                new_texto = ','.join([chr(i)])
                print(f'O novo texto é  {new_texto} ')

            # TODO: Criar regra que ao chegar na última letra, o novo código retornará para o início da tabela ASCII


texto = input("Digite o texto que será codificado ou decodificado: ")
chave = int(input("Digite o valor que será utilizado como chave (1 a 26): "))
modo = int(input("O que você deseja fazer, codificar [1] ou decodificar [2]? "))

if modo == 1:
    encrypt(texto, chave)
elif modo == 2:
    decrypt(texto, chave)
