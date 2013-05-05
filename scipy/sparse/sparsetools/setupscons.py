#!/usr/bin/env python

from __future__ import division, print_function, absolute_import

from os.path import join
import sys


def configuration(parent_package='',top_path=None):
    import numpy
    from numpy.distutils.misc_util import Configuration

    config = Configuration('sparsetools',parent_package,top_path,
                           setup_name='setupscons.py')

    config.add_sconscript('SConstruct')

    return config

if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(**configuration(top_path='').todict())
