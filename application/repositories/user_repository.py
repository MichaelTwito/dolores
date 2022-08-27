

from application.models import User
from .orm_repository_base import RepositoryBase
from ..utils.helper import get_from_obj_or_direct


class UserRepository(RepositoryBase):

    def __init__(self, app, db):
        super().__init__(db)

    def get_by_username(self, name):
        return self.session().query(User).filter_by(name=name).one()

    def list_users(self):
        return self.session().query(User).all()

    def create(self, user):
        user.name = get_from_obj_or_direct(user.name, "name")
        user.email = get_from_obj_or_direct(user.email, "email")
        user.password = get_from_obj_or_direct(user.password, "password")
        return super().create(user)