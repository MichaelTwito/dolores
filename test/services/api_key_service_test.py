from pytest import raises
from dolores_test import app
from application.services.api_key_service import create_api_key


def test_create_api_key(app):
    with app.app_context():
        """when params are valid, create the api key"""
        api_key = create_api_key('name')
        assert ['id','name','key'] == list(api_key.keys())
        """unique constraint"""
        with raises(RuntimeError, match='UNIQUE constraint failed'):   
            api_key = create_api_key('name')
