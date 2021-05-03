cmake_minimum_required(VERSION 3.0.2)
project(acrv_ros_wrappers)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  sensor_msgs
  message_generation
  )

catkin_python_setup()

add_service_files(
  FILES
  refinenet.srv
  )

generate_messages(
  DEPENDENCIES
  sensor_msgs
  )

catkin_package(
  CATKIN_DEPENDS message_runtime
  )
