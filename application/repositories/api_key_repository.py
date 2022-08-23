
from application.models import ApiKey
from .orm_repository_base import RepositoryBase
from application.services.utils import get_from_obj_or_direct


class ApiKeyRepository(RepositoryBase):

    def __init__(self, app, db):
        super().__init__(db)

    def get_by_key(self, name):
        return self.session().query(ApiKey).filter_by(key=key).one()


    def list_api_keys(self):
        return self.session().query(ApiKey).all()

            
    def create(self, api_key):
        api_key.name = get_from_obj_or_direct(api_key.name, "name")
        api_key.key = get_from_obj_or_direct(api_key.key, "key")
        return super().create(api_key)