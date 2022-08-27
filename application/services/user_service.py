from ..models import User
from ..context import SQLContext
from ..utils.error_handler import error_handler
from werkzeug.security import generate_password_hash

default_filters = ['password']

@error_handler
def create_user(name, email, password, filters = default_filters):
    Context = SQLContext()
    return Context.user_repository.create(User(name, email, generate_password_hash(password, method='sha256'))).as_dict(filters)

@error_handler
def get_user(name, filters = default_filters):
    Context = SQLContext()
    return Context.user_repository.get_by_username(name).as_dict(filters)

@error_handler
def list_users(filters = default_filters):
    Context = SQLContext()
    return list(map(lambda x: x.as_dict(filters),Context.user_repository.list_users()))
