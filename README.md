# Best of ACRV ROS Wrappers

TODO: badges

Here lie the ROS wrappers for our Best of ACRV codebases, and a severe lack of documentation.

TODO: gif showing the different services available

More to come.

## Installation

The wrappers are a ROS package, which are installed from source like any other ROS package:

1. Clone this repository into your Catkin workspace (or clone elsewhere, and symbolically link it in):

   ```
   u@pc:~/catkin_ws/src$ git clone https://github.com/best-of-acrv/acrv-ros-wrappers
   ```

2. Re-build your Catkin workspace:

   ```
   u@pc:~/catkin_ws/$ catkin_make
   ```

The wrappers depend on the underlying software (e.g. you can't run the RefineNet wrapper without the [RefineNet package](https://github.com/best-of-acrv/refinenet) installed). We have made the dependency dynamic, which means you don't need to have every piece of software installed to run the wrappers. This means if you only want to run [GGCNN](https://github.com/best-of-acrv/ggcnn) for instance, you can use the wrappers without installing everything else.

For the wrappers to work, you need to ensure that both ROS and your standard Python packages are accessible from the same terminal. In particular, Conda users may need to either adjust search paths (or [install ROS through Conda](https://github.com/RoboStack)) to ensure both ROS and Conda packages work harmoniously.

## Using the wrappers

The ROS package includes two scripts for interacting with available services:

- `start_services` for starting a set of services while dynamically requesting dependencies
- `call_services` as a demonstration of how services can be called

## Adding your own wrappers

TODO: handling passing of runtime parameters to the service implementation!

This package is used to showcase how the [Best of ACRV](https://roboticvision.org/best-of-acrv) software can be used with ROS. But if you decide you'd like to access your own services through this framework, new services can be added through a few simple steps:

1. Declare the input and output for your service by adding a new `.srv` file to the [`./srv`](./srv) directory. Also, add the messages into the compilation process by editing [`./CMakeLists.txt`](./CMakeLists.txt) and [`./package.xml`](./package.xml) as required.
2. Add a Python file implementing your service to the [`./src/acrv_ros_wrappers`] directory. Services are implemented as classes that extend the abstract `Service` class ([`./src/acrv_ros_wrappers/service.py`](./src/acrv_ros_wrappers/service.py)), providing implementations for all required abstract functionality. See [`./src/acrv_ros_wrappers/refinenet.py`](./src/acrv_ros_wrappers/refinenet.py) for an example.
3. Add your new service to the services list declared by `SERVICES` in [`./src/acrv_ros_wrappers/services.py`](./src/acrv_ros_wrappers/services.py). You need to provide an import path to your service class, where input paths are `'<relative_import_path_to_file>.<service_class_name>'`.
