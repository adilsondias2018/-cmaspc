from app.models.cadastro_model import Cadastro
from flask import Blueprint, current_app, jsonify, render_template


def cadastro_usuario(data: dict):
    

    print(data)

    cadastro: Cadastro = Cadastro(**data)

    session = current_app.db.session
    session.add(cadastro)
    session.commit()

    return jsonify(cadastro.nome)


# def filter_user(data: dict):    

#         user = Cadastro.query.filter_by(cpf=data['cpf']).first()
#         print(user.nome)

#         if user:
#                 return render_template('usuario.html', user=user)

#         return render_template('not_found.html')



