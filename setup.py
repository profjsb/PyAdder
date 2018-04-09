#!/usr/bin/env python
from __future__ import with_statement

import sys
try:
    from setuptools import setup, Extension, Command
except ImportError:
    from distutils.core import setup, Extension, Command
from distutils.command.build_ext import build_ext
from distutils.errors import CCompilerError, DistutilsExecError, \
    DistutilsPlatformError

VERSION = '0.0.3'
DESCRIPTION = "Total simple adder. Showing off package structure"

CLASSIFIERS = filter(None, map(str.strip,
"""
Development Status :: 1 - Unstable
Intended Audience :: Students
License :: OSI Approved :: BSD License
Programming Language :: Python
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3.5
Programming Language :: Python :: Implementation :: CPython
Topic :: Software Development :: Libraries :: Python Modules
""".splitlines()))

setup(
        name="PyAdder",
        version=VERSION,
        description=DESCRIPTION,
        long_description=DESCRIPTION,
        classifiers=CLASSIFIERS,
        author="Josh Bloom",
        author_email="profjsb@gmail.com",
        url="http://github.com/profjsb/PyAdder",
        license="BSD",
        packages=['adder', 'adder.tests'],
        platforms=['any'],
        setup_requires=['pytest-runner'],
        tests_require=['pytest']
)
