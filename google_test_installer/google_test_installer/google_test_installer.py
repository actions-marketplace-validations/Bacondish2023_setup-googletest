#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
A script which installs google test
'''

import os
import sys
import shutil
import platform
import subprocess
import tempfile
import logging


class GoogleTestInstaller:
    '''
    @brief      A class which installs GoogleTest.
    @details    Installation step is done by the CMake.
                The CMake creates "include" and "lib" directories under installation area
                and installs files there.
                User can specify installation area with an argument.
                Default installation areas are below.
                Linux:      "/usr/local"
                Windows:    Env["USERPROFILE"]
                Darwin:     "/usr/local"
    '''

    def __init__(self, branch_name, build_type, path_installation_area=None, is_print_subprocess=True):
        '''
        @brief Constructor.
        @param[in] branch_name              The name of tag or branch.
        @param[in] build_type               One of {Debug, Release, RelWithDebInfo, MinSizeRel}.
        @param[in] path_installation_area   The path to installation area. Absolute path.
        '''

        # attributes
        self.__url = r'https://github.com/google/googletest'
        self.__branch_name = branch_name
        self.__build_type = build_type
        self.__path_installation_area = path_installation_area
        self.__is_print_subprocess = is_print_subprocess

        # init logging
        self.__logger = logging.getLogger(__name__)
        self.__logger.setLevel(logging.DEBUG)

        # find installation area
        if self.__path_installation_area is None:
            self.__path_installation_area = self._get_path_installation_area()

        # sanity check of attributes
        if len(self.__branch_name) == 0:
            raise ValueError('Specifed branch name "{0}" is invalid'.format(self.__branch_name))

        if len(self.__build_type) == 0:
            raise ValueError('Specifed build type "{0}" is invalid'.format(self.__build_type))

        if self.__build_type not in ('Debug', 'Release', 'RelWithDebInfo', 'MinSizeRel'):
            self.__logger.warning('Specifed build type "{0}" is not predefined one. Typo?'.format(self.__build_type))

        if not os.path.isdir(self.__path_installation_area):
            raise FileNotFoundError('Installation area "{0}" does not exist'.format(self.__path_installation_area))

        if os.path.isfile(self.__path_installation_area + os.sep + 'include' + os.sep + 'gtest' + os.sep + 'gtest.h'):
            raise FileExistsError('GoogleTest is installed in specified directory "{0}"'.format(self.__path_installation_area))

        # logging
        self.__logger.info('Installer is initialized')
        self.__logger.info('Branch name is "{0}"'.format(self.__branch_name))
        self.__logger.info('Build type is "{0}"'.format(self.__build_type))
        self.__logger.info('Installation area is "{0}"'.format(self.__path_installation_area))


    def install(self):
        '''
        @brief Installs deriverables
        @details This operation has download, extract archive, build and install steps.
                 And these probably takes much time.
                 So, the count of call should be minimized.
        '''
        with tempfile.TemporaryDirectory() as tmpdir:
            build_directory_name = 'build'
            googletest_directory_name = 'googletest'
            path_googletest = tmpdir + os.sep + googletest_directory_name
            path_build = path_googletest + os.sep + build_directory_name

            self.__logger.info('Start installation')

            # checkout
            self.__logger.info('Checkout Google Test')
            #os.chdir(tmpdir)

            if self.__branch_name == 'main':
                arguments = [
                    'git', 'clone',
                    '--depth', '1',
                    self.__url,
                    path_googletest,
                    ]
            else:
                arguments = [
                    'git', 'clone',
                    '--branch', self.__branch_name,
                    '--depth', '1',
                    self.__url,
                    path_googletest,
                    ]

            self.__logger.debug('Run command "{0}"'.format(' '.join(arguments)))
            if self.__is_print_subprocess:
                subprocess.run(arguments, check=True)
            else:
                subprocess.run(arguments, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

            # generate build system
            self.__logger.info('Generate build system with CMake')
            os.makedirs(path_build)
            #os.chdir(path_build)

            arguments = [
                'cmake',
                '-DCMAKE_BUILD_TYPE=' + self.__build_type,
                '-G', self._get_cmake_generator_name(),
                '--install-prefix', self.__path_installation_area,
                '-B', path_build,
                '-S', path_googletest,
                ]

            self.__logger.debug('Run command "{0}"'.format(' '.join(arguments)))
            if self.__is_print_subprocess:
                subprocess.run(arguments, check=True)
            else:
                subprocess.run(arguments, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

            # build
            self.__logger.info('Build')
            #os.chdir(path_googletest)

            arguments = [
                'cmake',
                '--build', path_build,
                ]

            self.__logger.debug('Run command "{0}"'.format(' '.join(arguments)))
            if self.__is_print_subprocess:
                subprocess.run(arguments, check=True)
            else:
                subprocess.run(arguments, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

            # install
            self.__logger.info('Install')
            arguments = [
                'cmake',
                '--install', path_build,
                ]

            self.__logger.debug('Run command "{0}"'.format(' '.join(arguments)))
            if self.__is_print_subprocess:
                subprocess.run(arguments, check=True)
            else:
                subprocess.run(arguments, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

            # clean
            self.__logger.info('Clean')
            if platform.system() == 'Windows':
                # In windows repository (.git/) has files which cannot be removed with python operation
                arguments = ['del', '/F', '/S', '/Q', path_googletest]
                self.__logger.debug('Run command "{0}"'.format(' '.join(arguments)))
                subprocess.run(arguments, shell=True, check=True, stdout=subprocess.DEVNULL)
            else:
                shutil.rmtree(path_googletest)

            self.__logger.info('Installation done')


    def _get_path_installation_area(self):
        '''
        @brief Returns path of installation area based on platform
        '''
        path = None

        if platform.system() == 'Linux':
            path = '/usr/local'
        elif platform.system() == 'Windows':
            if 'USERPROFILE' in os.environ:
                path = os.environ['USERPROFILE']
            else:
                raise RuntimeError('This Windows platform does not have environment variable "USERPROFILE".')
        elif platform.system() == 'Darwin':
            path = '/usr/local'
        else:
            raise RuntimeError('Platform "{0}" is not supported', platform.system())

        return path


    def _get_cmake_generator_name(self):
        '''
        @brief Returns generator name of cmake based on platform
        '''
        generator_name = None

        if platform.system() == 'Linux':
            generator_name = 'Unix Makefiles'
        elif platform.system() == 'Windows':
            generator_name = 'NMake Makefiles'
        elif platform.system() == 'Darwin':
            generator_name = 'Unix Makefiles'
        else:
            raise RuntimeError('Platform "{0}" is not supported', platform.system())

        return generator_name


if __name__ == '__main__':
    # executed
    pass
else:
    # imported
    pass
