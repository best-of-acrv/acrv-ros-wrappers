from refinenet import RefineNet as RefineNetBase
from ros_numpy import numpify, msgify
from sensor_msgs.msg import Image

from acrv_ros_wrappers.srv import RefineNet as RefineNetService

from .service import Service


class RefineNet(Service):

    def __init__(self):
        super(RefineNet, self).__init__('refinenet', RefineNetService)
        self.base = RefineNetBase(load_pretrained='voc', num_classes=21)

    def callback(self, req):
        return RefineNetService._response_class(segmented_image=msgify(
            Image,
            self.base.predict(image=numpify(req.rgb_image),
                              colour_map_preset='voc'),
            encoding=req.rgb_image.encoding))
