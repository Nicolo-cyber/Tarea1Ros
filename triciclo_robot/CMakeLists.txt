cmake_minimum_required(VERSION 3.8)
project(triciclo_robot)

find_package(ament_cmake REQUIRED)

install(DIRECTORY launch urdf worlds config
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
