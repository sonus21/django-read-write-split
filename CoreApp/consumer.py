from .constants import SECONDARY, PRIMARY
from CoreApp.middlewares import db_wrapper


@db_wrapper(PRIMARY)
def reserve_driver(request):
    # logic goes here
    pass


@db_wrapper(SECONDARY)
def aggregate_driver_rating(request):
    # logic goes here
    pass
