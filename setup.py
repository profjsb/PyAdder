#!/usr/bin/env python
import sys
from setuptools import setup

VERSION = '0.0.5'
DESCRIPTION = "Total simple adder. Showing off package structure"

CLASSIFIERS = list(filter(None, map(str.strip,
"""
Development Status :: 2 - Pre-Alpha
Intended Audience :: Education
License :: OSI Approved :: BSD License
Programming Language :: Python
Programming Language :: Python :: 3.5
Programming Language :: Python :: 3.6
Programming Language :: Python :: 3.7
Programming Language :: Python :: 3.8
Programming Language :: Python :: 3.9
Programming Language :: Python :: Implementation :: CPython
Topic :: Software Development :: Libraries :: Python Modules
""".splitlines())))

setup(
        name="PyAdder",
        version=VERSION,
        description=DESCRIPTION,
        long_description=DESCRIPTION,
        long_description_content_type="text/x-rst",
        classifiers=CLASSIFIERS,
        author="Josh Bloom",
        author_email="profjsb@gmail.com",
        url="http://github.com/profjsb/PyAdder",
        python_requires='>=3',
        license="BSD",
        keywords='sample setuptools eduction data-science',
        packages=['adder', 'adder.tests'],
        platforms=['any'],
        setup_requires=['pytest-runner'],
        tests_require=['pytest']
)
