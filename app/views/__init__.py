from flask import Flask


def init_app(app: Flask):
    from .cadastro_view import bp as bp_cadastro

    app.register_blueprint(bp_cadastro)
