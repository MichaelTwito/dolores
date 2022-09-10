import functools
from flask import jsonify
from sqlalchemy import exc

def error_handler(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except RuntimeError as e:
            return jsonify({"message": str(e)}), 500
        except exc.IntegrityError as e:
            raise RuntimeError(str(e.orig))
        except Exception as e:
            return None
    return decorator
