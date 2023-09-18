cmake_minimum_required(VERSION 2.8)
project(setup_googletest_exmaple_project)

# CTest
enable_testing()

# GoogleTest
find_package(GTest REQUIRED)

##################################################
# platform settings
##################################################
if (UNIX)
    # nothing to do
elseif (WIN32)
    add_definitions("/source-charset:utf-8")

    # Google Test requires following runtime-library option on MSVC build.
    set(CMAKE_CXX_FLAGS_DEBUG "/MTd")
    set(CMAKE_CXX_FLAGS_RELEASE "/MT")

else ()
    # nothing to do
endif ()

##################################################
# build
##################################################
add_subdirectory(example_project)
