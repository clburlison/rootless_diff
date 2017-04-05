#!/usr/bin/python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
"""
A helper script to copy SIP related files.
"""

from __future__ import print_function
import os
import shutil
import sys
import plistlib


def get_version():
    '''Obtain system version info from the disk version plist'''
    SYSTEM_VERSION = ('/System/Library/CoreServices/SystemVersion.plist')
    try:
        sys_ver = plistlib.readPlist(SYSTEM_VERSION)
    except:
        sys.stderr.write("ERROR: Unable to read SystemVersion.plist")
        sys.exit(1)
    return sys_ver


def main():
    '''Main method for copying files for git references'''
    ver = get_version()
    directory = '{}_{}'.format(ver.get('ProductUserVisibleVersion'),
                               ver.get('ProductBuildVersion'))
    if os.path.exists(directory):
        sys.stderr.write("ERROR: Directory '{}' exists. "
                         "Exiting...".format(directory))
        sys.exit(1)
    else:
        os.makedirs(directory)

    # Copy the launchd rootless file
    LAUNCHD_FILE_NAME = 'com.apple.xpc.launchd.rootless.plist'
    LAUNCHD_FILE = os.path.join('/System/Library/Sandbox/', LAUNCHD_FILE_NAME)
    shutil.copyfile(LAUNCHD_FILE, os.path.join(directory, LAUNCHD_FILE_NAME))

    # Copy the rootless conf file
    CONF_FILE_NAME = 'rootless.conf'
    CONF_FILE = os.path.join('/System/Library/Sandbox/', CONF_FILE_NAME)
    shutil.copyfile(CONF_FILE, os.path.join(directory, CONF_FILE_NAME))

    print("SUCESSFUL: Copy complete...")


if __name__ == '__main__':
    main()
