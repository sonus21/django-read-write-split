from functools import wraps

from .utils import db_from_the_request
from .db_router import set_db_for_router, clear_db_for_router


class DatabaseMiddleware(object):
    """
    DatabaseMiddleware sets the db in the thread local context and used
    across multiple calls to handle the DB calls.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        db = db_from_the_request(request)
        set_db_for_router(db)
        try:
            return self.get_response(request)
        finally:
            clear_db_for_router()


def db_wrapper(name):
    """
    Decorator to make any method use specific database from list of databases. Usage::

    @db_wrapper("primary")
    def my_function(a,b,c, *args, **kwargs):
      pass
    """

    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            set_db_for_router(name)
            try:
                return func(*args, **kwargs)
            finally:
                clear_db_for_router()
        return inner
    return decorator
