import cryptocode
import os

chave = os.getenv('SECRET_KEY')
mensagem = "J9jvIlBxRg==*JzFKEaR"


MensagemDescriptografada = cryptocode.decrypt(mensagem, chave)
print("Sua mensagem descriptografada: " + MensagemDescriptografada)