cmake_minimum_required(VERSION 3.16)
project(algorytmy LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/bin")

# Każdy *.cpp w katalogu głównym → osobny executable (np. 1.cpp → bin/1)
file(GLOB CPP_SOURCES CONFIGURE_DEPENDS "${CMAKE_CURRENT_SOURCE_DIR}/*.cpp")

if(NOT CPP_SOURCES)
    message(STATUS "Brak plików .cpp — dodaj np. 2.cpp i przebuduj.")
endif()

foreach(SOURCE ${CPP_SOURCES})
    get_filename_component(TARGET_NAME "${SOURCE}" NAME_WE)
    add_executable("${TARGET_NAME}" "${SOURCE}")
endforeach()
