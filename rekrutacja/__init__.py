# create and configure the app
import os

from flask import Flask

from rekrutacja import auth
import rekrutacja.model
# from rekrutacja.cli import commands
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

    # GUI
    # app.register_blueprint(bp.bp)

    # API
    app.register_blueprint(auth.bp)

    # commandline arguments
    # app.cli.add_command(new_package)

    return app


app = create_app()
