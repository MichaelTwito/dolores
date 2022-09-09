import pytest
from dolores_test import app
from application.services.user_service import create_user, get_user, list_users

def test_create_user(app):
    with app.app_context():
        """when params are valid, return the user attributes as dict without the password"""
        assert {'email': 'email', 'id': 1, 'name': 'name'} ==\
              create_user('name', 'email', 'password')
    
        """when params are valid, and filter set to [],return all user attributes as dict"""
        user_dict = create_user('name_1', 'email_1', 'password', [])
        assert all(map(lambda x: x in user_dict, ('email','id','name', 'password')))
        
        """unique constraint"""
        with pytest.raises(RuntimeError, match='UNIQUE constraint failed'): 
            create_user('name', 'email_1', 'password')
            create_user('name_1', 'email', 'password')

def test_get_user(app):
    with app.app_context():
        """when params are valid, get the user by name"""
        create_user('name', 'email', 'password')
        assert {'email': 'email', 'id': 1, 'name': 'name'} ==\
                get_user('name')
        
        """when params are valid, with empty filter, get the user by name including password"""
        user_dict = get_user('name',[])
        assert all(map(lambda x: x in user_dict, ('email','id','name', 'password')))
        
        """when the user does not exist, return None"""
        assert None == get_user('none',[])

def test_list_users(app):
    with app.app_context():
        """when the database is empty"""
        assert [] == list_users()

        """when there are two users, return them"""
        create_user("name","email","password")
        create_user("name_1","email_1","password_!")
        users_list = list_users()
        assert len(users_list) == 2

        """when there are two users, and filter is empty, return users and password"""
        users_list_with_passwords = list_users([])
        assert len(users_list_with_passwords) == 2
        assert all(map(lambda x: 'password' in x, users_list_with_passwords))


