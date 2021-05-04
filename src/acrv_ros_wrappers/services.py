import importlib
import re

_services = {'refinenet': '.refinenet.RefineNet'}


def load_service(name, *args, **kwargs):
    service_str = next((p for n, p in _services.items() if n == name), None)
    if not service_str:
        raise ValueError("Could not find a '%s' service to load. Please "
                         "confirm the name. Valid names are:\n\t%s" %
                         (name, ",".join(service_list())))
    return getattr(
        importlib.import_module(re.sub(r'(.*)\..*', r'\1', service_str),
                                package='acrv_ros_wrappers'),
        service_str.split('.')[-1])(*args, **kwargs)


def service_list():
    return list(_services.keys())
