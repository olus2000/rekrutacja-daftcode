# create and configure the app
import os

from flask import Flask, url_for, redirect

from rekrutacja import auth, message, gui
import rekrutacja.model
from rekrutacja.cli import init_db, manage_users
from rekrutacja.db import db


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    # load the instance config, if it exists, when not testing
    app.config.from_pyfile('config.py', silent=True)
    if test_config is not None:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # connect to database
    app.config['SQLALCHEMY_DATABASE_URI'] = app.config['SQLALCHEMY_DATABASE_URI'] \
        .format(instance=app.instance_path)
    db.init_app(app)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Henlo, Warld!'
    
    @app.route('/')
    def index():
        return redirect(url_for('gui.login'))

    # GUI
    app.register_blueprint(gui.bp)

    # API
    app.register_blueprint(auth.bp)
    app.register_blueprint(message.bp)

    # commandline arguments
    app.cli.add_command(init_db)
    app.cli.add_command(manage_users)

    return app


app = create_app()
