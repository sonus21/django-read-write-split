from .constants import PRIMARY, SECONDARY


def _determine_db_name(method, path):
    # If you have multiple read databases, you can use DNS to direct them to one database.
    # Alternatively, you can randomly select a database from the list if you prefer not to
    # use DNS.
    if method in ["GET"]:
        return SECONDARY
    # in many cases POST method can be read only as well
    # and in some cases GET method can be performing CUD operations as well
    # in these cases we can add a check on the path
    return PRIMARY


def db_from_the_request(request):
    http_method = request.method
    http_path = request.path
    return _determine_db_name(http_method, http_path)
