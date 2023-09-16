# pip install python-dotenv folium flask cryptocode
from flask import Flask, render_template, request, url_for, redirect
import pymysql
import folium
import json
import os
import cryptocode

app = Flask(__name__)

# Configurações do banco de dados
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'db': 'projeto_venda',
    'cursorclass': pymysql.cursors.DictCursor
}

try:
    connection = pymysql.connect(**db_config)
    print("[+]------- CONECTADO -------[+]")
except pymysql.Error as e:
    print(f"Erro ao conectar ao banco de dados: {e}")

# Criar um cursor
cursor = connection.cursor()

criar_tabela = """
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    senha VARCHAR(250) NOT NULL
);"""

try:
    cursor.execute(criar_tabela)
    print("TABELA CRIADA")
except pymysql.Error as e:
    print(f"Tabela não foi criada -> {e}")
    pass

@app.route('/register', methods=['GET','POST'])    
def register():
    SECRET_KEY = os.getenv('SECRET_KEY')
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('password')
        senha_hash = cryptocode.encrypt(senha, SECRET_KEY)
        senha_criptografada = senha_hash
        print("Usuário: ",nome)
        print("Email: ",email)
        print("Senha Criptografada: ",senha_criptografada)
        senha_descriptografada = cryptocode.decrypt(senha_criptografada, SECRET_KEY)
        print("Senha Descriptografada: ",senha_descriptografada)

        # Verificar se o usuário já existe
        verifica_query = "SELECT * FROM usuarios WHERE nome = %s OR email = %s"
        cursor.execute(verifica_query, (nome, email))
        usuario_existente = cursor.fetchone()

        if usuario_existente:
            variavel = "Usuário com o mesmo nome ou email já existe."
            return render_template('register.html', variavel=variavel)
        else:
            variavel = "Usuário inserido com sucesso!"
            insert_query = "INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)"
            data = (nome, email, senha_criptografada)
            cursor.execute(insert_query, data)
            connection.commit()
            print('Usuário inserido com sucesso!')
            return render_template('register.html', variavel_P=variavel)

    return render_template('register.html')

@app.route('/login', methods=['GET','POST'])    
def login():
    if request.method == "POST":
        SECRET_KEY = os.getenv('SECRET_KEY')
        nome = request.form.get("nome")
        senha = request.form.get("password")

        conn = pymysql.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE nome = %s", (nome,))
        user = cursor.fetchone()
        conn.close()

        if user and cryptocode.decrypt(user['senha'], SECRET_KEY) == senha:
            print(f"[+] Usuário Logado: {nome}")
            print(user)
            return render_template('mapa.html')
        else: 
            variavel = "Credenciais inválidas"
            return render_template('login.html', variavel=variavel)

    return render_template('login.html')   

# Rota principal para exibir o mapa
@app.route('/mapa')
def mapa():
    return redirect(url_for('login'))
    #return render_template('mapa.html')

# Rota para lidar com o upload do arquivo JSON e adicionar marcadores ao mapa
@app.route('/add_markers', methods=['GET','POST'])
def add_markers():
    if 'json_file' in request.files:
        json_file = request.files['json_file']
        if json_file.filename != '':
            # Lê o arquivo JSON e adiciona marcadores ao mapa
            map_data = json.load(json_file)
            map_with_markers = create_map_with_markers(map_data)
            return map_with_markers._repr_html_()
    return render_template('mapa.html')
    #return redirect(url_for('mapa'))

def create_map_with_markers(data):
    # Crie um mapa Folium
    m = folium.Map(location=[0, 0], zoom_start=3)

    # Adicione marcadores com base nos dados do arquivo JSON
    for item in data:
        if 'lat' in item and 'lon' in item:
            lat, lon = item['lat'], item['lon']
            marker = folium.Marker([lat, lon])
            marker.add_to(m)
    return m    

if __name__ == '__main__':
    app.run(debug=True)