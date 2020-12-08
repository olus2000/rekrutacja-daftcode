from flask import Blueprint, request, render_template, session, jsonify, redirect, url_for


bp = Blueprint('gui', __name__, url_prefix='/gui')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    return render_template('login.html')


@bp.route('/create')
def create():
    return render_template('create.html')


@bp.route('/<int:id>/read')
def read(id):
    return render_template('read.html', id=id)


@bp.route('/<int:id>/edit')
def edit(id):
    return render_template('edit.html', id=id)


@bp.route('/set_token', methods=('POST',))
def set_token():
    session['token'] = request.json['token']
    return jsonify({'token': request.json['token']})


@bp.route('/unset_token')
def unset_token():
    session.clear()
    return redirect(url_for('gui.login'))
