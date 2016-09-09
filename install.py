#!/usr/bin/env python3

import platform
import os
import subprocess


def main():
    distName = platform.dist()[0]
    if distName == 'Ubuntu':
        retval = subprocess.call(['which', 'git'])
        print(retval)

        if retval:
            subprocess.call(['apt-get', 'install', 'git'])

        if not os.path.exists('~/work1'):
            os.makedirs = ('~/work1')
        subprocess.call(['git', 'clone', 'http://github.com/fedusia/common-dot-files', '~/work1'])


if __name__ == '__main__':
    main()
