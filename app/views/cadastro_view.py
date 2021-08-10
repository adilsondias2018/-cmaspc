from app.models.cadastro_model import Cadastro
from app.services.cadastro_services import cadastro_usuario
from flask import Blueprint, jsonify, redirect, render_template, request

bp = Blueprint('bp_cadastro', __name__)

@bp.route('/')
def home():

        return render_template('index.html')

@bp.route('/login', methods=['GET'])
def get_login():

        return render_template('login.html')

@bp.route('/login', methods=['POST'])
def post_login():

        return render_template('usuario.html')
        
@bp.route('/usuario')
def get_usuario():
        

        return render_template('usuario.html')


@bp.route('/cadastrar', methods=['POST'])
def post():

        data = {"nome": request.form['nome'], "dataNascimento": request.form['dataNascimento'],"email": request.form['email'], "cpf": request.form['cpf'],"identidade": request.form['identidade'], "telefone": request.form['telefone'], "segmentoAtuacao": request.form['segmentoAtuacao'],"tipoSegmento": request.form['tipoSegmento'],"participacao": request.form['participacao'],"conselheiro": request.form['conselheiro'], "candidato": request.form['candidato'], "eixos": request.form['eixos'], "termo": request.form['termo']}

        cadastro_usuario(data)        
        
        return render_template('cadastro.html')
