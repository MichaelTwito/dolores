
import uuid
from ..models import ApiKey
from ..context import SQLContext


def create_api_key(name, filters =[]):
    Context = SQLContext()
    return Context.api_key_repository.create(ApiKey(name, uuid.uuid4())).as_dict(filters)