from ..models import User
from ..context import SQLContext
from werkzeug.security import generate_password_hash

default_filters = ['password']

def create_user(name, email, password, filters = default_filters):
    Context = SQLContext()
    return Context.user_repository.create(User(name, email, generate_password_hash(password, method='sha256'))).as_dict(filters)
        
def get_user(name, filters = default_filters):
    try:
        Context = SQLContext()
        return Context.user_repository.get_by_username(name).as_dict(filters)
    except Exception:
        return None

def list_users(filters = default_filters):
    try:
        Context = SQLContext()
        return list(map(lambda x: x.as_dict(filters),Context.user_repository.list_users()))
    except Exception:
        return None