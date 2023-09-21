# pip install python-dotenv folium flask cryptocode
from flask import Flask, render_template, request, url_for, redirect, session
import pymysql
import folium
from folium.plugins import MarkerCluster, Draw
import json
import os
import cryptocode
from mysql_cmd import insert, verificar, autenticar, cursor

app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
def register():
    SECRET_KEY = os.getenv('SECRET_KEY')
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('password')
        senha_hash = cryptocode.encrypt(senha, SECRET_KEY)
        senha_criptografada = senha_hash
        print("Usuário: ", nome)
        print("Email: ", email)
        print("Senha Criptografada: ", senha_criptografada)
        senha_descriptografada = cryptocode.decrypt(senha_criptografada, SECRET_KEY)
        print("Senha Descriptografada: ", senha_descriptografada)

        # Check if user exists in the database
        usuario_existente = verificar(nome, email)

        if usuario_existente:
            variavel = "Usuário com o mesmo nome ou email já existe."
            return render_template('register.html', variavel=variavel)
        else:
            # User does not exist, insert the data into the database
            variavel = "Usuário inserido com sucesso!"
            insert(nome, email, senha_criptografada)  # Insere usuário no banco de dados
            print('Usuário inserido com sucesso!')
            return render_template('register.html', variavel_P=variavel)

    return render_template('register.html')


@app.route('/login', methods=['GET','POST'])    
def login():
    if request.method == "POST":
        SECRET_KEY = os.getenv('SECRET_KEY')
        nome = request.form.get("nome")
        senha = request.form.get("password")

        user = autenticar(nome, senha) # mysql_cmd.py

        if user and cryptocode.decrypt(user['senha'], SECRET_KEY) == senha:
            print(f"[+] Usuário Logado: {nome}")
            print(user)
            return render_template('mapa.html', nome=nome)
        else: 
            variavel = "Credenciais inválidas"
            return render_template('login.html', variavel=variavel)

    return render_template('login.html')   

if __name__ == '__main__':
    app.run(debug=True)