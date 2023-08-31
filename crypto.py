import cryptocode

chave = "423338233093093"
mensagem = "Esta eh a minha mensagem! :)"

MensagemCriptografada = cryptocode.encrypt(mensagem, chave)
print("Sua mensagem criptografada: " + MensagemCriptografada)

MensagemDescriptografada = cryptocode.decrypt(MensagemCriptografada, chave)
print("Sua mensagem descriptografada: " + MensagemDescriptografada)