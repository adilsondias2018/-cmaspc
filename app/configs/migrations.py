from flask import Flask
from flask_migrate import Migrate

from .database import db


def init_app(app):


    Migrate(app, app.db, compare_type=True)
