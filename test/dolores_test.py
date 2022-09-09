import os
import pytest
from application import init_app
from application import db
from application.services.user_service import create_user
@pytest.fixture()
def app():
    app = init_app(os.environ['TEST_APP_SETTINGS'])
    app.config.update({
        "TESTING": True,
    })
    with app.app_context():
        db.create_all()
    # other setup can go here

    yield app

    # clean up / reset resources here

@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
