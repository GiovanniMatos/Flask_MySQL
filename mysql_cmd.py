import pymysql
import cryptocode
import os

# Configurações do banco de dados
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'db': 'projeto_flask',
    'cursorclass': pymysql.cursors.DictCursor
}

try:
    connection = pymysql.connect(**db_config)
    print("[+]------- CONECTADO -------[+]")
except pymysql.Error as e:
    print(f"Erro ao conectar ao banco de dados: {e}")

# Criar um cursor
cursor = connection.cursor()
# Criar tabela
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

SECRET_KEY = os.getenv('SECRET_KEY')

def verificar(nome, email):
    # Verificar se o usuário já existe
    verifica_query = "SELECT * FROM usuarios WHERE nome = %s OR email = %s"
    cursor.execute(verifica_query, (nome, email))
    usuario_existente = cursor.fetchone()
    
    return usuario_existente  # Return the result of verification


def insert(nome, email, senha_criptografada):

    insert_query = "INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)"
    data = (nome, email, senha_criptografada)
    cursor.execute(insert_query, data)
    connection.commit()

def autenticar(nome, senha):
    cursor.execute("SELECT * FROM usuarios WHERE nome = %s", (nome,))
    user = cursor.fetchone()

    if user:
        stored_encrypted_password = user['senha']  # Assuming 'senha' is the encrypted password field
        entered_password = senha

        # Decrypt the stored encrypted password and compare it with the entered password
        decrypted_password = cryptocode.decrypt(stored_encrypted_password, SECRET_KEY)

        if decrypted_password == entered_password:
            return user

    return None