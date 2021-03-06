#!/usr/bin/env python
"""enplot: a one-line command line plotting tool for CSV data

enplot is a simple plotting tool for quickly visualizing data in CSV and
related formats. It uses Python/Scipy/matplotlib as backend.
"""

DOCLINES = __doc__.split('\n')

CLASSIFIERS = """\
Programming Language :: Python
Topic :: Engineering
Operating System :: POSIX
Operating System :: Unix
"""

import os
import sys
import shutil
import re
import subprocess
import warnings
from distutils.core import setup, Extension
import numpy as np


MAJOR = 1
MINOR = 0
MICRO = 0
ISRELEASED = False
VERSION = '%d.%d.%d' % (MAJOR, MINOR, MICRO)
REVISION = 0 + int(os.popen("git rev-list --all | wc -l").read())


def write_version_py(filename='enplot/version.py'):
    if os.path.exists(filename):
        os.remove(filename)
    cnt = """\
# THIS FILE IS AUTOMATICALLY GENERATED BY ENPLOT SETUP.PY
version = '%(version)s'
revision = %(revision)s
release = %(isrelease)s
"""
    a = open(filename, 'w')
    try:
        a.write(cnt % {'version': VERSION,
                       'revision': REVISION,
                       'isrelease': str(ISRELEASED)})
    finally:
        a.close()

write_version_py()

setup(
    name="enplot",
    version=VERSION,
    packages=['enplot'],
    scripts=['enplot/enplot'],
    include_dirs=[np.get_include()],
    author="Robert Johansson",
    author_email="jrjohansson@gmail.com",
    license="LGPL",
    description=DOCLINES[0],
    long_description="\n".join(DOCLINES[2:]),
    keywords="plotting, one-line, command-line",
    url="http://github.com/jrjohansson",
    platforms=["Linux", "Unix"],
    package_data={'enplot': ['*.png'], }
)
