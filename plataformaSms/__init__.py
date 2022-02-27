from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# import pyperclip


app = Flask(__name__)

# ***** Configurações Gerais da Aplicação *****
# ---------------------------------------------
# TOKEN de acesso
app.config['SECRET_KEY'] = '59940c20166524157d996d8ba6749e6b'

# Configurações de acesso ao Banco de Dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/smsMobileOptin.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['GOOGLE_API_KEY'] = 'AIzaSyBXA-C0q36RU7fXbotKdOnT1tpCf02LNec'


# Criar o Banco de dados Físic
database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Direciona para esta página quando exigir que o usuário esteja logado
login_manager.login_message = 'Você deve estar logado para acessar a página que você esta querendo !!'
login_manager.login_message_category = 'alert-info'

from plataformaSms import routes

