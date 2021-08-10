from environs import Env
from flask import Flask, render_template, request

from app import views
from app.configs import database, migrations

env = Env()
env.read_env()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = env("SQLALCHEMY_DATABASE_URI")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JSON_SORT_KEY'] = False

    database.init_app(app)
    views.init_app(app)
    migrations.init_app(app)


    # @app.route('/')
    # def home():

    #     return render_template('index.html')

    # @app.route('/cadastrar', methods=['POST'])
    # def post():

    #     data = {"nome": request.form['nome'], "dataNascimento": request.form['dataNascimento'],"email": request.form['email'], "cpf": request.form['cpf'],"identidade": request.form['identidade'], "telefone": request.form['telefone'], "segmentoAtuacao": request.form['segmentoAtuacao'],"tipoSegmento": request.form['tipoSegmento'],"participacao": request.form['participacao'],"conselheiro": request.form['conselheiro'], "candidato": request.form['candidato'], "eixos": request.form['eixos'], "termo": request.form['termo']}
    
    #     print(data)        
    #     return render_template('cadastro.html')

    return app
