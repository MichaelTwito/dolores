from application import db
from sqlalchemy import Column, Integer, String


class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)
    password = Column(String(120), unique=False)

    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.password = password

    def as_dict(self, filters=[]):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns if c.name not in filters}
    
    def __repr__(self):
        return f'<User {self.name!r}>'


class ApiKey(db.Model):
    __tablename__ = 'api_keys'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    key = Column(String(120), unique=True)

    def __init__(self, name=None, key=None):
        self.name = name
        self.key = key

    def as_dict(self, filters=[]):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns if c.name not in filters}
    
    def __repr__(self):
        return f'<ApiKey {self.name!r}>'
