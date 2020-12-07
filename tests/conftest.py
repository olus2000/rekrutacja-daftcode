import pytest
from rekrutacja import create_app
from rekrutacja.db import db


@pytest.fixture
def app():
    app = create_app({
        'ENV': 'developement',
        'TESTING': True,
    })

    app.test_cli_runner().invoke(args=['init-db --clear --src=test-db'])

    yield app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
