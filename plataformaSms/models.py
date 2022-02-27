from plataformaSms import database, login_manager
from datetime import datetime
from flask_login import UserMixin

# Como criar o Database na mao no Python Console.
# Ver video abaixo:
# https://hashtag.eadplataforma.com/lesson/detail/15/3294/
# Entre Minuto 06:00 - 08:00

@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))

class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    foto_perfil = database.Column(database.String, default='default.jpg')
    # Criar relacionamentos entre tabelas
    # Posts dos usuários
    posts = database.relationship('Post', backref='autor', lazy=True)
    cursos = database.Column(database.String, nullable=False, default='Não Informado')

    def contar_posts(self):
        return len(self.posts)

# ----------------------------------------------------------------
class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    titulo = database.Column(database.String, nullable=False)
    corpo = database.Column(database.Text, nullable=False)
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
    # Observação: Na linha acima, colocar smpre o utcnow apenas pq se colocar utcnow(), o banco
    # vai gravar sempre a data e hora do momento  que foi criado a tabela.
    # Criar o Id de identificação do usário que criou o Post.
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)
    # Obs: Por padrão ao informar a tabela estrangeira

# ----------------------------------------------------------------

""" Cadastros das tabelas da Central de envio de Mensagens """

class CadModules(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    descrModule = database.Column(database.String, nullable=False)
    fixed_ip = database.Column(database.String, nullable=False, unique=True)
    udpPort = database.Column(database.Integer, nullable=False)
    ativo = database.Column(database.Boolean, nullable=False)

    """ Criar relacionamentos entre tabelas """


# ----------------------------------------------------------------

""" Cadastro dos Servidores que controlarão a central Telefonica """
class CadServers(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    descrServer = database.Column(database.String, nullable=False)
    fixed_ip = database.Column(database.String, nullable=False, unique=True)
    udpPort = database.Column(database.Integer, nullable=False)
    ativo = database.Column(database.Boolean, nullable=False)

    """ Criar relacionamentos entre tabelas """

# ----------------------------------------------------------------

""" Dados Capturados dos Celulares """
class phone_data(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    data_received = database.Column(database.String, nullable=False)
    hora_received = database.Column(database.String, nullable=False)
    operadora = database.Column(database.String, nullable=False)
    evento = database.Column(database.String, nullable=False)
    emei = database.Column(database.String, nullable=False)
    imsi = database.Column(database.String, nullable=False)
    modulo = database.Column(database.String, nullable=False)
    msg_sent = database.Column(database.Boolean, nullable=False)

    """ Criar relacionamentos entre tabelas """

# ----------------------------------------------------------------