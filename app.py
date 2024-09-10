from flask import Flask, request, jsonify
import json 
import os
app = Flask (__name__)
usuarios = []


@app.route('/usuario', methods = ['POST'])
def criarUser():
    lerUser()
    user = request.get_json()
    usuarios.append(user)
    salvarUser()
    print(user)
    return ("usuario cadastrado")

@app.route('/usuario/<int:cpf>', methods = ['GET'])
def consultaUser(cpf):
    lerUser()
    for usuario in usuarios:
        if cpf == usuario.get('cpf'):
            return usuario
    return "usuario nao encontrado"

def salvarUser():
    with open ("usuarioh.json", "w") as arquivo: json.dump(usuarios, arquivo, indent=4)

def lerUser():
    if os.path.exists("usuarioh.json"):
        with open ("usuarioh.json", "r") as arquivo: usuarios=json.load(arquivo)

app.run(port=5000,host='localhost', debug=True)
