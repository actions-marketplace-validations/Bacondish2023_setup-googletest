#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest

import os
import platform
import tempfile
import logging
import subprocess

import google_test_installer.google_test_installer as google_test_installer


class TestGoogleTestInstaller(unittest.TestCase):


    @unittest.skipUnless(platform.system() == 'Windows', 'This test case does not support platform "{0}"'.format(platform.system()))
    def test_typical_msvc_1_13_0(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            # run
            obj = google_test_installer.GoogleTestInstaller('v1.13.0', 'Release', tmpdir, False)
            obj.install()

            # verify
            self.assertTrue(os.path.isfile(tmpdir + os.sep + 'include' + os.sep + 'gtest' + os.sep + 'gtest.h'))
            self.assertTrue(os.path.isfile(tmpdir + os.sep + 'include' + os.sep + 'gmock' + os.sep + 'gmock.h'))
            self.assertTrue(os.path.isfile(tmpdir + os.sep + 'lib' + os.sep + 'gtest.lib'))
            self.assertTrue(os.path.isfile(tmpdir + os.sep + 'lib' + os.sep + 'gtest_main.lib'))
            self.assertTrue(os.path.isfile(tmpdir + os.sep + 'lib' + os.sep + 'gmock.lib'))
            self.assertTrue(os.path.isfile(tmpdir + os.sep + 'lib' + os.sep + 'gmock_main.lib'))


    @unittest.skipUnless(platform.system() == 'Windows', 'This test case does not support platform "{0}"'.format(platform.system()))
    def test_typical_msvc_1_11_0(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            # run
            obj = google_test_installer.GoogleTestInstaller('release-1.11.0', 'Release', tmpdir, False)
            obj.install()

            # verify
            self.assertTrue(os.path.isfile(tmpdir + os.sep + 'include' + os.sep + 'gtest' + os.sep + 'gtest.h'))
            self.assertTrue(os.path.isfile(tmpdir + os.sep + 'include' + os.sep + 'gmock' + os.sep + 'gmock.h'))
            self.assertTrue(os.path.isfile(tmpdir + os.sep + 'lib' + os.sep + 'gtest.lib'))
            self.assertTrue(os.path.isfile(tmpdir + os.sep + 'lib' + os.sep + 'gtest_main.lib'))
            self.assertTrue(os.path.isfile(tmpdir + os.sep + 'lib' + os.sep + 'gmock.lib'))
            self.assertTrue(os.path.isfile(tmpdir + os.sep + 'lib' + os.sep + 'gmock_main.lib'))


    @unittest.skipUnless(
        (platform.system() == 'Linux') or (platform.system() == 'Darwin'),
        'This test case does not support platform "{0}"'.format(platform.system()))
    def test_typical_posix_1_13_0(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            # run
            obj = google_test_installer.GoogleTestInstaller('v1.13.0', 'Release', tmpdir, False)
            obj.install()

            # verify
            self.assertTrue(os.path.isfile(tmpdir + os.sep + 'include' + os.sep + 'gtest' + os.sep + 'gtest.h'))
            self.assertTrue(os.path.isfile(tmpdir + os.sep + 'include' + os.sep + 'gmock' + os.sep + 'gmock.h'))
            self.assertTrue(os.path.isfile(tmpdir + os.sep + 'lib' + os.sep + 'libgtest.a'))
            self.assertTrue(os.path.isfile(tmpdir + os.sep + 'lib' + os.sep + 'libgtest_main.a'))
            self.assertTrue(os.path.isfile(tmpdir + os.sep + 'lib' + os.sep + 'libgmock.a'))
            self.assertTrue(os.path.isfile(tmpdir + os.sep + 'lib' + os.sep + 'libgmock_main.a'))


    @unittest.skipUnless(
        (platform.system() == 'Linux') or (platform.system() == 'Darwin'),
        'This test case does not support platform "{0}"'.format(platform.system()))
    def test_typical_posix_1_11_0(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            # run
            obj = google_test_installer.GoogleTestInstaller('release-1.11.0', 'Release', tmpdir, False)
            obj.install()

            # verify
            self.assertTrue(os.path.isfile(tmpdir + os.sep + 'include' + os.sep + 'gtest' + os.sep + 'gtest.h'))
            self.assertTrue(os.path.isfile(tmpdir + os.sep + 'include' + os.sep + 'gmock' + os.sep + 'gmock.h'))
            self.assertTrue(os.path.isfile(tmpdir + os.sep + 'lib' + os.sep + 'libgtest.a'))
            self.assertTrue(os.path.isfile(tmpdir + os.sep + 'lib' + os.sep + 'libgtest_main.a'))
            self.assertTrue(os.path.isfile(tmpdir + os.sep + 'lib' + os.sep + 'libgmock.a'))
            self.assertTrue(os.path.isfile(tmpdir + os.sep + 'lib' + os.sep + 'libgmock_main.a'))


    def test_error_branch_name_1(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            with self.assertRaises(ValueError):
                obj = google_test_installer.GoogleTestInstaller('', 'Release', tmpdir) # raise


    def test_error_branch_name_2(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            with self.assertRaises(subprocess.CalledProcessError):
                obj = google_test_installer.GoogleTestInstaller('does_not_exist', 'Release', tmpdir, False)
                obj.install() # raise


    def test_error_build_type(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            with self.assertRaises(ValueError):
                obj = google_test_installer.GoogleTestInstaller('release-1.11.0', '', tmpdir) # raise


    def test_error_path_installation_area_1(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path_does_not_exist = tmpdir + os.sep + 'foo'
            with self.assertRaises(FileNotFoundError):
                obj = google_test_installer.GoogleTestInstaller('release-1.11.0', 'Release', path_does_not_exist) # raise


    def test_error_path_installation_area_2(self):
        with tempfile.TemporaryDirectory() as tmpdir:

            # create installed situation
            path_header_dir = tmpdir + os.sep + 'include' + os.sep + 'gtest'
            os.makedirs(path_header_dir)
            with open(path_header_dir + os.sep + 'gtest.h', mode='w') as fp:
                pass
            with open(path_header_dir + os.sep + 'gmock.h', mode='w') as fp:
                pass

            with self.assertRaises(FileExistsError):
                obj = google_test_installer.GoogleTestInstaller('release-1.11.0', 'Release', tmpdir) # raise


if __name__ == '__main__':
    # executed
    unittest.main()
