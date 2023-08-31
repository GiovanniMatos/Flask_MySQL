from flask import Flask, render_template, request, url_for
import pymysql
import os
import cryptocode


app = Flask(__name__)

# Configurações do banco de dados
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'db': 'projeto_Flask',
    'cursorclass': pymysql.cursors.DictCursor
}

try:
    connection = pymysql.connect(**db_config)
    print("CONECTADO")
except pymysql.Error as e:
    print(f"Erro ao conectar ao banco de dados: {e}")

# Criar um cursor
cursor = connection.cursor()

criar_tabela = """
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    senha VARCHAR(100) NOT NULL
);"""

try:
    cursor.execute(criar_tabela)
    print("TABELA CRIADA")
except pymysql.Error as e:
    print(f"Tabela não foi criada -> {e}")
    pass

@app.route('/register', methods=['GET','POST'])    
def register():
    SECRET_KEY = 'P4$$w0rds'
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('password')
        senha_hash = cryptocode.encrypt(senha, SECRET_KEY)
        senha_criptografada = senha_hash
        print(nome)
        print(email)
        print(senha_criptografada)

        # Verificar se o usuário já existe
        verifica_query = "SELECT * FROM usuarios WHERE nome = %s OR email = %s"
        cursor.execute(verifica_query, (nome, email))
        usuario_existente = cursor.fetchone()

        if usuario_existente:
            variavel = "Usuário com o mesmo nome ou email já existe."
            return render_template('register.html', variavel=variavel)
        else:
            insert_query = "INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)"
            data = (nome, email, senha_criptografada)
            cursor.execute(insert_query, data)
            connection.commit()
            print('Usuário inserido com sucesso!')

    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)