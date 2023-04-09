import threading

threadLocal = threading.local()


def get_current_db_name():
    return getattr(threadLocal, "DB", None)


def set_db_for_router(db):
    setattr(threadLocal, "DB", db)


def clear_db_for_router():
    threadLocal.__dict__.clear()


class DBRouter(object):
    def db_for_read(self, model, **hints):
        return get_current_db_name()

    def db_for_write(self, model, **hints):
        return get_current_db_name()

    def allow_relation(self, *args, **kwargs):
        return True

    def allow_syncdb(self, *args, **kwargs):
        return None

    def allow_migrate(self, *args, **kwargs):
        return None
