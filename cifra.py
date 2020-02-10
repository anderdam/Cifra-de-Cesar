#Imports
import requests
import hashlib
import json
from json import dump, load
from os.path import isfile


#Faz a requisição para a URL e salva os dados como json no Python
r = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=55f9a57245df88f6653c40457f7ac0d5ed21c085')
r_dict = r.json()
dados = r_dict

path = 'Json/answer.json'

#Funções:
#Cria o arquivo answer.json na pasta Json se aindas não tiver sido criado
def criarJson(path):
    if not isfile(path):
        with open(path, 'w') as f:
            dump(dados, f, indent=2)
        return True
    else:
        return False


#Função para atualizar e criar um novo answer.json
novo_path = 'answer.json'
def atualizarJson(novo_path):
    if not isfile(novo_path):
        with open(novo_path, 'w') as f:
            dump(novos_dados, f, indent=2)
        return True
    else:
        return False


#Função para ler o arquivo answer.json
def lerJson(path):
    if isfile(path):
        with open(path) as f:
            data = load(f)
        return data
    else:
        return False


#Função para decifrar o código
alfabeto = 'abcdefghijklmnopqrstuvwxyz'
def decifrar(cifrado, chave):
    m = ''
    for c in cifrado:
        if c in alfabeto:
            indice = alfabeto.index(c)
            m += alfabeto[(indice - chave) % len(alfabeto)]
        else:
            m += c
    return m


criarJson(path)

#Lê o arqjuivo answer.json e cria as variáveis para decifrar o código
answer_json = lerJson(path)
chave = answer_json['numero_casas']
cifrado = answer_json['cifrado']
decifrado = decifrar(cifrado, chave)

#  Gerar um resumo criptográfico do texto decifrado usando o algoritmo sha1
hsh = hashlib.sha1()
hsh.update(decifrado.encode('utf-8'))
resumo_criptografico = hsh.hexdigest()

novos_dados = {'numero_casas': chave, 'token': '55f9a57245df88f6653c40457f7ac0d5ed21c085', 'cifrado': cifrado,
                'decifrado': decifrado, 'resumo_criptografico': resumo_criptografico}
json_data = json.dumps(novos_dados)
atualizarJson(novo_path)

print(answer_json)
print(chave)
print(cifrado)
print(decifrado)
print(resumo_criptografico)


#  Faz o envio da resposta para a URL:
""" 
url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=55f9a57245df88f6653c40457f7ac0d5ed21c085'
arquivo = {'answer': ('answer', open('answer.json', 'rb'))}
envio = requests.post(url=url+token, files=arquivo) 
"""
