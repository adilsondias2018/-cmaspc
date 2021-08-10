from app.models.cadastro_model import Cadastro
from flask import Blueprint, current_app, jsonify


def cadastro_usuario(data: dict):
    

    print(data)

    cadastro: Cadastro = Cadastro(**data)

    session = current_app.db.session
    session.add(cadastro)
    session.commit()

    return jsonify(cadastro.nome)


    