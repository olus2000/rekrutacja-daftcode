import pytest
from datetime import datetime, timedelta

from rekrutacja.model import Token


@pytest.mark.parametrize(('login', 'password', 'code'), (
    ('A', 'B', 403),
    ('Kate', 'B', 403),
    ('Axel', 'Axel', 200)
))
def test_token_codes(client, login, password, code):
    response = client.post('/auth/token', json={'login': login, 'password': password})
    assert response.status_code == code


def test_token_creation(client, app):
    token_value = client.post('/auth/token', json={'login': 'Kate', 'password': 'Kate'}) \
        .json['token']
    assert len(token_value) == 342
    with app.app_context():
        assert Token.query.filter(Token.value == token_value).one_or_none() is not None


def test_token_expiration(client, app):
    day = timedelta(days=1)
    time_1 = datetime.now()
    token_value = client.post('/auth/token', json={'login': 'Kate', 'password': 'Kate'}) \
        .json['token']
    time_2 = datetime.now()
    with app.app_context():
        token = Token.query.filter(Token.value == token_value).one()
        assert token.expires >= time_1 + day and token.expires <= time_2 + day
    assert client.post('/auth/refresh', json={'token': token_value}).json['token'] == token_value
    time_3 = datetime.now()
    with app.app_context():
        token = Token.query.filter(Token.value == token_value).one()
        assert token.expires >= time_2 + day and token.expires <= time_3 + day


def test_auth_required(client, auth):
    assert client.post('/auth/refresh', json={'token': 'asdf'}).status_code == 403
