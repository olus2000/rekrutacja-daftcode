from datetime import datetime

from flask import Blueprint, request, abort
from flask.json import jsonify

from rekrutacja.db import db
from rekrutacja.model import Message
from rekrutacja.auth import auth_required


bp = Blueprint('message', __name__, url_prefix='')


@bp.route('/<int:id>/read', methods=('GET',))
def read(id):
    message = Message.query.filter(Message.id == id).one_or_none()
    if message is None:
        abort(404)
    message.views += 1
    db.session.commit()
    return jsonify({'id': id,
                    'content': message.content,
                    'edited': datetime.strftime(message.edited, '%Y-%m-%d %H:%M:%S.%f'),
                    'views': message.views})


@bp.route('/<int:id>/edit', methods=('POST',))
@auth_required
def edit(id):
    message = Message.query.filter(Message.id == id).one_or_none()
    if message is None:
        abort(404)
    if 'content' not in request.json or len(str(request.json['content'])) > 160:
        abort(400)
    message.content = str(request.json['content'])
    message.edited = datetime.now()
    message.views = 0
    db.session.commit()
    return jsonify({'id': id,
                    'content': message.content,
                    'edited': datetime.strftime(message.edited, '%Y-%m-%d %H:%M:%S.%f'),
                    'views': message.views})


@bp.route('/create', methods=('POST',))
@auth_required
def create():
    if 'content' not in request.json or len(str(request.json['content'])) > 160:
        abort(400)
    message = Message(content=request.json['content'], edited=datetime.now())
    db.session.add(message)
    db.session.commit()
    return jsonify({'id': message.id,
                    'content': message.content,
                    'edited': datetime.strftime(message.edited, '%Y-%m-%d %H:%M:%S.%f'),
                    'views': message.views})


@bp.route('/<int:id>/delete', methods=('POST',))
@auth_required
def delete(id):
    message = Message.query.filter(Message.id == id).one_or_none()
    if message is None:
        abort(404)
    db.session.delete(message)
    db.session.commit()
    return jsonify({'id': id,
                    'content': message.content,
                    'edited': datetime.strftime(message.edited, '%Y-%m-%d %H:%M:%S.%f'),
                    'views': message.views})

