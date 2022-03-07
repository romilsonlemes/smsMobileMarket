# smsMobileMarket
Software para envio de mensagem por Central Telefonica

Site construído com o Framework Flask

Python Version 3.10
Para Instalar a aplicação, seguir os comandos abaixo:

```
python3.10 -m venv .venv
source .venv/bin/activate
pip install pip -U pip
pip install -r requirements.txt
```

Aplicação para Conferencia da Qualidade de Código

```
flake8
```

Criar todo o Database
Sair no Python Console e gerar todas as bases com os seguintes comandos
```
from plataformaSms import database
database.create_all()
```
# Obs: Se o comando acima não funcionar, saia do PyCharm e entre novamente e faça o mesmo procedimento