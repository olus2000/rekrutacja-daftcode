import pytest
from datetime import datetime

from rekrutacja.model import Message


@pytest.mark.parametrize(('id', 'code'), (
    (1, 200),
    (5, 404),
))
def test_message_read_codes(client, id, code):
    assert client.get(f'/{id}/read').status_code == code


def test_message_read_data(client):
    message = client.get('/0/read').json
    for key, value in {'id': 0,
                       'content': 'FIRST!!!1!1!',
                       'edited': '2020-10-17 13:46:12.000000',
                       'views': 6}.items():
        assert key in message and message[key] == value


@pytest.mark.parametrize(('id', 'content', 'code'), (
    (15, 'Nonexistent', 404),
    (0, 'TooLongInputTooLongInputTooLongInputTooLongInputTooLongInputTooLongInputTooLongInput' +
        'TooLongInputTooLongInputTooLongInputTooLongInputTooLongInputTooLongInput12345', 400),
    (0, 'Edit: Sorry...', 200)
))
def test_message_edit_codes(client, auth, id, content, code):
    token = auth.token()
    assert client.post(f'/{id}/edit', json={'token': token, 'content': content}).status_code == code


def test_message_edit_data(auth, client):
    token = auth.token()
    time_1 = datetime.now()
    data = client.post('/1/edit', json={'token': token, 'content': 'New content'}).json
    for key, val in {'id': 1, 'content': 'New content', 'views': 0}.items():
        assert key in data and data[key] == val
    time_edited = datetime.strptime(data['edited'], '%Y-%m-%d %H:%M:%S.%f')
    assert time_1 <= time_edited and time_edited <= datetime.now()


def test_message_create_error_400(auth, client):
    token = auth.token()
    assert client.post('/create', json={
        'token': token,
        'content': 'TooLongInputTooLongInputTooLongInputTooLongInputTooLongInputTooLongInput' +
        'TooLongInputTooLongInputTooLongInputTooLongInputTooLongInputTooLongInputTooLongInput12345',
    }).status_code == 400


def test_message_create_correct(auth, client):
    token = auth.token()
    time_1 = datetime.now()
    data = client.post('/create', json={'token': token, 'content': 'New content'}).json
    for key, val in {'id': 2, 'content': 'New content', 'views': 0}.items():
        assert key in data and data[key] == val
    time_edited = datetime.strptime(data['edited'], '%Y-%m-%d %H:%M:%S.%f')
    assert time_1 <= time_edited and time_edited <= datetime.now()


def test_message_delete_error_404(auth, client):
    token = auth.token()
    assert client.post('/15/delete', json={'token': token}).status_code == 404


def test_message_delete_correct(auth, client, app):
    token = auth.token()
    data = client.post('/1/delete', json={'token': token}).json
    for key, val in {'id': 1,
                     'content': 'You\'ve got to be kidding...',
                     'views': 500,
                     'edited': '2020-10-19 13:30:59.000000'}.items():
        assert key in data and data[key] == val
    with app.app_context():
        assert Message.query.filter(Message.id == 1).one_or_none() is None
