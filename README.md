# Flask MySQL 🗃

## Instalação

### Linux
```bash
  sudo apt install -y python3 python3-pip python3.10-venv
```
```bash
  git clone https://github.com/GiovanniMatos/Flask_MySQL.git && cd Flask_MySQL && pip3 install Flask python-dotenv pymysql folium cryptocode
```
###### Virtualenv
```bash
  pip3 install virtualenv && python3 -m venv venv && source venv/bin/activate
```
### Windows
```bash
  git clone https://github.com/GiovanniMatos/Flask_MySQL.git
  cd Flask_MySQL
  pip install Flask python-dotenv pymysql folium cryptocode
```
###### Virtualenv
```bash
  pip install virtualenv
  python -m venv venv
  venv\Scripts\activate
```
### VSCode
```bash
  code .
```
Cadastro - A senha adicionada no formulário é criptografada e enviada ao Banco de Dados.

![image](https://github.com/GiovanniMatos/Flask_MySQL/assets/99231397/b0d319ad-74dd-41c3-a9cb-b23d92e0f79d)
![image](https://github.com/GiovanniMatos/Flask_MySQL/assets/99231397/a143dba9-a02f-4ada-8dfe-1aa6b3d56520)

Login - A senha colocada no formulário é comparada com a senha do Banco de Dados que será descriptografada para fazer a verificação e também se a senha corresponde ao usuário.

![image](https://github.com/GiovanniMatos/Flask_MySQL/assets/99231397/179a04f8-3fea-47b7-bb44-c439ed6567b0)

Caso a senha seja esquecida, o arquivo "crypto.py" irá retornar a senha descriptografada.

![image](https://github.com/GiovanniMatos/Flask_MySQL/assets/99231397/f1868ffe-aa2a-43dc-97cd-0646830de61d)

O mapa poderá ser acessado apenas após o Login, caso seja adicionada a rota para ele na URL, será redirecionada ao Login. Nele há opção de adicionar linhas que mostram a distância de um ponto a outro, círculo para marcação do local, marcadores, etc.

![image](https://github.com/GiovanniMatos/Flask_MySQL/assets/99231397/2a48e6ff-0374-492e-8a41-133747bfcc6c)

Para testar a segurança da sua senha, poderá usar o script de Brute Force, teste wordlists mais utilizadas entre hackers para simular uma tentativa real de quebra de senha.

![image](https://github.com/GiovanniMatos/Flask_MySQL/assets/99231397/19f940ed-9419-41d5-b4e4-9a710c0a7b13)
![image](https://github.com/GiovanniMatos/Flask_MySQL/assets/99231397/0c936067-1811-48d1-8e5b-049207a476b9)

