cmake_minimum_required(VERSION 2.8)
project(tast)

set (tast_VERSION_MAJOR 0)
set (tast_VERSION_MINOR 1)

find_package( OpenCV REQUIRED)
add_executable(tast main.cpp)
target_link_libraries(tast ${OpenCV_LIBS})

include (InstallRequiredSystemLibraries)
include (CPack)
