import importlib
import re

_services = {'refinenet': '.refinenet.RefineNet'}


def load_service(name, *args, **kwargs):
    service_str = next((p for n, p in _services.items() if n == name), None)
    if not service_str:
        raise ValueError("Could not find a '%s' service to load. Please "
                         "confirm the name. Valid names are:\n\t%s" %
                         (name, ",".join(service_list())))
    # TODO make this dynamic instead of hacked!
    return getattr(
        importlib.import_module('.refinenet', package='acrv_ros_wrappers'),
        'RefineNet')(*args, **kwargs)


def service_list():
    return list(_services.keys())
