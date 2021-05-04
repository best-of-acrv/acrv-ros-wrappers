from abc import ABC, abstractmethod
import rospy


class Service(ABC):

    def __init__(self, name, service_class):
        self.name = name
        self.service = rospy.Service(name, service_class, self.callback)

    @abstractmethod
    def callback(self, req):
        pass
