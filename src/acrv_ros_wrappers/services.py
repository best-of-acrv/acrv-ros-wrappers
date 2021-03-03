from .service import Service

_services = [Service(name='refinenet')]


def get_service(name):
    return next((s for s in _services if s.name == name), None)


def service_list():
    return [s.name for s in _services]
