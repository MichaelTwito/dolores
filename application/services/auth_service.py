import functools
from flask import request, current_app
from . import user_service, api_key_service
from werkzeug.security import check_password_hash


app = current_app._get_current_object()
super_admin_username = app.config['SUPER_ADMIN_USERNAME']

def is_api_key_valid(api_key):
    return api_key_service.is_exist(api_key)

def api_required(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        api_key = request.headers.get('x-api-key')
        if not api_key: return {"message": "Please provide an API key"}, 400
        return func(*args, **kwargs) if is_api_key_valid(api_key)\
                                     else ({"message": "The provided API key is not valid"}, 403)           
    return decorator

def is_valid_superadmin(username, password):
    #Empty filters as by default the password is not returned
    filters = []
    user = user_service.get_user(username, filters)
    return True if user and user['name'] == super_admin_username\
             and check_password_hash(user['password'], password)\
             else False
        
def super_admin_required(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        return func(*args, **kwargs)\
                if is_valid_superadmin(kwargs['username'], kwargs['password'])\
                else ({"message": "The provided credentials is not valid"}, 403) 
    return decorator