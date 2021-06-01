# Importando bibliotecas necessárias para configuração do script
import requests
import json
import os

# Importando módulo request para viabilizar response http via post request
from requests.models import Response

# Comando "cls" através do módulo os.system para limpar tela no terminal do usuário
os.system('cls') 

# Recebendo os dados "user" e "passoword" do usuário via terminal
user = input("Digite seu usuário: ")
password=input("Enter password: ")

# criação de um dicionário "dados" com o "rm" e "senha" fornecidos pelo usuário
dados = {
    "rm": (user),
    "senha": (password)
}

# Realiza uma requisição http do tipo POST, enviando os dados em formato json
r = requests.post('https://dc1-2021.glitch.me/getHash', json=dados)

# Converte a variável com resposta da requisição para o formato json
res = r.json()

# Converte a variável "res" para o formato texto para validação do campo "nome"
rtxt=(r.text)

# Valida se a varinável "rtxt", que trata a resposta do gethash, possui o campo "nome" na resposta.
if rtxt.find("nome") == 2:

# Se existir o nome, imprime na tela uma mensagem, seguida com o hash obtido
    print("Parabéns! Login realizado com sucesso! Seu hash é:", res["hash"])

# Se não existir o nome na validação if acima, imprime na tela uma mensagem de login inválido
else:
    print("Login e senha digitados estão incorretos! Tente novamente.")
