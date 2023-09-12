import cryptocode
from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])    
def decrypt():
    SECRET_KEY = os.getenv('SECRET_KEY')
    if request.method == 'POST':
        senha = request.form.get('password')
        print("Senha Criptografada: ",senha)
        senha_descriptografada = cryptocode.decrypt(senha, SECRET_KEY)
        print("Senha Descriptografada: ",senha_descriptografada)
        resultado = senha_descriptografada

        return render_template('decrypt.html', resultado=resultado)
    
    return render_template('decrypt.html')
    

if __name__ == "__main__":
    app.run(debug=True)