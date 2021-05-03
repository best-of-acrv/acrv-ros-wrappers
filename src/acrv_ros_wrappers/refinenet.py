from refinenet import RefineNet as RefineNetBase

from .service import Service


class Refinenet(Service):

    def __init__(self):
        super(Refinenet, self).__init__('refinenet', None)

        self.base = RefineNetBase()
