import cryptocode
import dotenv
import os

SECRET_KEY = os.getenv('SECRET_KEY')
mensagem = '1i9Ke/k=*ygfBUXf4qng'


MensagemDescriptografada = cryptocode.decrypt(mensagem, SECRET_KEY)
print("Sua mensagem descriptografada: " + MensagemDescriptografada)