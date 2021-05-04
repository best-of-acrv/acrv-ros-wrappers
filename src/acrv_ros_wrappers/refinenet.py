from refinenet import RefineNet as RefineNetBase

from acrv_ros_wrappers.srv import RefineNet as RefineNetService

from .service import Service


class RefineNet(Service):

    def __init__(self):
        super(RefineNet, self).__init__('refinenet', RefineNetService)
        self.base = RefineNetBase()

    def callback(self, req):
        print("Request received!")
        return RefineNetService._response_class()
