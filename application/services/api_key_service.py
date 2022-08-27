
import uuid
from ..models import ApiKey
from ..context import SQLContext
from ..utils.error_handler import error_handler

@error_handler
def create_api_key(name, filters =[]):
    Context = SQLContext()
    return Context.api_key_repository.create(ApiKey(name, uuid.uuid4())).as_dict(filters)

@error_handler
def is_exist(api_key):
    Context = SQLContext()
    return Context.api_key_repository.is_exist(api_key)