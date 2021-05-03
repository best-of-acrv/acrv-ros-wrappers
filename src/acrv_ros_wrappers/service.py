import rospy


class Service:

    def __init__(self, name, service_class):
        self.name = name
        self.service = rospy.ServiceProxy(name, service_class)
