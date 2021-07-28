from flask import Flask
from flask_jwt_extended import jwt_manager


def init_app(app):

    jwt_manager(app)
    
