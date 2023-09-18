# Setup GoogleTest

An GitHub Action which sets up your workflow with specified version of GoogleTest.

Intended user
* The person who wants to test C/C++ project with the GoogleTest on the GitHub Actions workflow.
  And uses CMake.

## Usage

#### CMakeLists.txt

This action supports the **FindGTest** which searches GoogleTest installation area.
And the FindGTest provides variables which index to include directory, library files.
So, you don't have to write path to installation area on CMakeLists.txt .

If you don't know FindGTest, see [CMake: FindGTest](https://cmake.org/cmake/help/latest/module/FindGTest.html) .

```cmake
find_package(GTest REQUIRED)

add_executable(test_foo foo.c)
target_include_directories( test_foo PRIVATE ${GTEST_INCLUDE_DIRS} )
target_link_libraries( test_foo tested_library ${GTEST_BOTH_LIBRARIES} )
```

Let's write `find_package` with GTest argument before target definition such as
`add_executable` and `add_library` .
And specify include directory / library
with variables `${GTEST_INCLUDE_DIRS}` and `${GTEST_BOTH_LIBRARIES}` .


#### Workflow

###### Basic

```yaml
steps:
  - uses: Bacondish2023/setup-googletest@v1
    with:
      tag: v1.14.0
  # And build steps
```

Inputs

|Item|Description|Mandatory?|Default|
|:---|:---|:---|:---|
|tag|Tag or branch name of GoogleTest.|No|main|
|build-type|Build type. One of {Debug, Release, RelWithDebInfo, MinSizeRel}.<br>Keep same with your project|No|Release|
|loglevel|Logging level. One of {OFF, CRITICAL, ERROR, WARNING, INFO, DEBUG}.|No|INFO|

###### Windows Specific

```yaml
steps:
  - uses: ilammy/msvc-dev-cmd@v1
  - uses: Bacondish2023/setup-googletest@v1
    with:
      tag: v1.14.0
  # And build steps
```

On Windows platform, this action requires MSVC.
[ilammy/msvc-dev-cmd](https://github.com/ilammy/msvc-dev-cmd) is recommended,
because it is used for example project on this repository and tested.


## Prerequisites

#### Supported Platform

|Platform|Shell|Toolchain|
|:---|:---|:---|
|Linux|Bash|GCC|
|Windows|Power Shell|MSVC|
|MacOS|Bash|GCC|


## License

This project is free and open-source software licensed under the **MIT License** .  
