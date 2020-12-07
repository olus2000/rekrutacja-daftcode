import functools
import os
from datetime import datetime, timedelta

from rekrutacja.model import User, Token

from flask import Blueprint, request, url_for, abort, jsonify
from werkzeug.utils import redirect
from werkzeug.security import check_password_hash


bp = Blueprint('auth', __name__, url_prefix='/auth')


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(*args, **kwargs):
        if 'token' not in request:
            abort(401)
        token = Token.query.filter(Token.value == request['token']).one_or_none()
        if token is None or token.expires < datetime.now():
            abort(401)
        return view(*args, **kwargs)
    return wrapped_view


@bp.route('/authenticate', methods=('POST',))
def authenticate():
    login = request.form['login']
    password = request.form['password']
    user = User.query.filter(User.login == login).one_or_none()

    # check credentials
    if user is None or not check_password_hash(user.password, password):
        abort(401)

    # cleanup token table
    tokens = Token.query.all()
    if len(tokens) > 256:
        for token in tokens:
            if token.expires < datetime.now():
                db.session.delete(token)
    
    # assign new token
    taken_values = [token.value for token in tokens]
    new_value = os.urandom(256)
    while os in taken_values:
        new_value = os.urandom(256)
    
    db.session.add(Token(value=new_value, expires=datetime.now() + timedelta(days=1)))
    db.session.commit()

    return jsonify(new_value)
