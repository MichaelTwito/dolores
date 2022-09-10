from dolores_test import app
from application.services.user_service import create_user
from application.services.api_key_service import create_api_key
from application.services.auth_service import is_api_key_valid, is_valid_superadmin

def test_is_api_key_valid(app):
    with app.app_context():
        """when params are valid"""
        api_key = create_api_key('user')
        assert True == is_api_key_valid(api_key['key'])
        """when the key does not exist"""
        assert False == is_api_key_valid('invalid_key')

def test_is_valid_superadmin(app):
    with app.app_context():
        """when params are valid"""
        super_admin_username = app.config['SUPER_ADMIN_USERNAME']
        password = '123456'
        super_admin_user = create_user(super_admin_username, 'email', password)
        print(super_admin_user)
        assert True == is_valid_superadmin(super_admin_user['name'], password)
        """when the user is not super admin"""
        assert False == is_valid_superadmin('user', password)
