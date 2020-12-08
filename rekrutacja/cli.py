import csv
from datetime import datetime

import click
from flask import current_app
from flask.cli import with_appcontext
from werkzeug.security import generate_password_hash

from rekrutacja.db import db
from rekrutacja.model import User, Token, Message


def _load_table(src, filename, mapper):
    with open(f'{src}/{filename}', encoding='utf-8') as csvfile:
        csvreader = csv.DictReader(csvfile, dialect='piped')
        records = []
        for row in csvreader:
            records.append(mapper(row))
        db.session.bulk_save_objects(records)
        db.session.commit()


@click.command('init-db')
@click.option('--clear/--no-clear', default=False)
@click.option('--src', default='', type=click.Path())
@with_appcontext
def init_db(clear, src):
    if clear:
        db.drop_all()
    db.create_all()
    
    if src:
        csv.register_dialect('piped', delimiter='|', quoting=csv.QUOTE_NONE, lineterminator='\n',
                             escapechar='\\')

        _load_table(src, 'user.csv', lambda row: User(
            login=row['login'],
            password=row['password'],
        ))

        _load_table(src, 'token.csv', lambda row: Token(
            value=row['login'],
            expires=datetime.strptime(row['expires'], '%Y-%m-%d %H:%M:%S.%f'),
        ))

        _load_table(src, 'message.csv', lambda row: Message(
            id=int(row['id']),
            content=row['content'],
            edited=datetime.strptime(row['edited'], '%Y-%m-%d %H:%M:%S.%f'),
            views=int(row['views']),
        ))


@click.command('manage-users')
@click.option('--add/--delete', default=True)
@click.option('-u')
@click.option('-p', default=None)
@with_appcontext
def manage_users(add, u, p):
    if add:
        if p is None:
            raise Exception('Password not provided')
        db.session.add(User(login=u, password=generate_password_hash(p)))
    else:
        user = User.query.filter(User.login == u).one_or_none()
        if user is None:
            raise Exception('User does not exist')
        db.session.delete(user)
    db.session.commit()
