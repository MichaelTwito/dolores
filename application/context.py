# from presentation import register_filters
from application import db
from flask import current_app
from .repositories import user_repository
from .repositories import api_key_repository


class SQLContext(object):

    def __init__(self):
        app = current_app._get_current_object()
        self.db = db
        self.user_repository = user_repository.UserRepository(app, db)
        self.api_key_repository = api_key_repository.ApiKeyRepository(app, db)
        
