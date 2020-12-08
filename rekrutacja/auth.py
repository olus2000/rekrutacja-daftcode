import functools
from secrets import token_urlsafe
from datetime import datetime, timedelta

from flask import Blueprint, request, abort, jsonify
from werkzeug.security import check_password_hash

from rekrutacja.model import User, Token
from rekrutacja.db import db


bp = Blueprint('auth', __name__, url_prefix='/auth')


def auth_required(view):
    @functools.wraps(view)
    def wrapped_view(*args, **kwargs):
        if request.json is None or 'token' not in request.json:
            abort(403)
        token = Token.query.filter(Token.value == request.json['token']).one_or_none()
        if token is None or token.expires < datetime.now():
            abort(403)
        return view(*args, **kwargs)
    return wrapped_view


@bp.route('/token', methods=('POST',))
def token():
    if request.json is None:
        abort(400)
    login = request.json['login']
    password = request.json['password']
    user = User.query.filter(User.login == login).one_or_none()

    # check credentials
    if user is None or not check_password_hash(user.password, password):
        abort(403)

    # cleanup token table
    tokens = Token.query.all()
    if len(tokens) > 256:
        for token in tokens:
            if token.expires < datetime.now():
                db.session.delete(token)

    # assign new token
    taken_values = [token.value for token in tokens]
    new_value = token_urlsafe(256)
    while new_value in taken_values:
        new_value = token_urlsafe(256)

    db.session.add(Token(value=new_value, expires=datetime.now() + timedelta(days=1)))
    db.session.commit()

    return jsonify({'token': new_value})


@bp.route('/refresh', methods=('POST',))
@auth_required
def refresh():
    token_val = request.json['token']
    token = Token.query.filter(Token.value == token_val).one()
    token.expires = datetime.now() + timedelta(days=1)
    db.session.commit()

    return jsonify({'token': token_val})
