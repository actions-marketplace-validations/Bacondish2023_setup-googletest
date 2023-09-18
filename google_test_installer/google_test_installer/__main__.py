#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
A script which installs google test
'''

import os
import sys
import getopt
import platform
import traceback
import logging


import google_test_installer.google_test_installer as google_test_installer


def main():
    branch_name = 'main'
    build_type = 'Release'
    loglevel = 'WARNING'

    try:
        opts, args = getopt.getopt(sys.argv[1:], 'h', ['help', 'branch=', 'build_type=', 'loglevel='])
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(1)

    for o, a in opts:
        if (o == '-h') or (o == '--help'):
            print_usage()
            sys.exit(0)
        if (o == '--branch'):
            branch_name = a
        if (o == '--build_type'):
            build_type = a
        if (o == '--loglevel'):
            loglevel_candidates = {'OFF', 'CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG'}
            if a in loglevel_candidates:
                loglevel = a
            else:
                printUsage()
                sys.exit(1)

    # ---> setting
    if loglevel == 'OFF':
        logging.basicConfig(level='WARNING')
        logging.disable(logging.CRITICAL)
    else:
        root_handler = logging.StreamHandler()
        root_handler.setLevel(loglevel)

        logging.basicConfig(
            format = '%(asctime)s %(levelname)s: %(message)s',
            level = loglevel,
            handlers = [root_handler]
        )
    # <--- setting

    # ---> operation

    try:
        logging.info('GoogleTestInstaller starts')
        logging.debug('Platform is {0}'.format(platform.system()))

        is_print_subprocess = False
        if loglevel == 'DEBUG':
            is_print_subprocess = True
        else:
            is_print_subprocess = False

        obj = google_test_installer.GoogleTestInstaller(branch_name, build_type, is_print_subprocess=is_print_subprocess)
        obj.install()
    except:
        traceback.print_exc()
        sys.exit(1)
    finally:
        logging.info('GoogleTestInstaller ends')
    # <--- operation


def print_usage():
    command_name = 'google_test_installer'

    print('Description:')
    print('    Installs google test')
    print('Usage:')
    print('    {0} [options]'.format(command_name))
    print('    {0} [h|--help]'.format(command_name))
    print('Option:')
    print('    --branch     name:   Branch or tag name.')
    print('                         Default is master')
    print('    --build_type name:   One of {Debug, Release, RelWithDebInfo, MinSizeRel}.')
    print('                         Default is Release')
    print('    --loglevel LEVEL     log-level: Set the level of logging')
    print('                         One of {OFF, CRITICAL, ERROR, WARNING, INFO, DEBUG}.')
    print('                         The default is WARNING.')
    print('    --help, -h:          Show help')


if __name__ == '__main__':
    # executed
    main()
