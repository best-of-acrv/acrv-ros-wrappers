cmake_minimum_required(VERSION 3.0.2)
project(wrappers-ros)

find_package(catkin REQUIRED)

catkin_python_setup()

## Generate services in the 'srv' folder
# add_service_files(
#   FILES
#   Service1.srv
#   Service2.srv
# )

## Generate added messages and services with any dependencies listed here
# generate_messages(
#   DEPENDENCIES
#   std_msgs  # Or other packages containing msgs
# )

catkin_package()
