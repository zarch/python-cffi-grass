#!/usr/bin/env python

import os
import sys

from setuptools import setup, find_packages

os.chdir(os.path.dirname(sys.argv[0]) or ".")

setup(
    name="cffi-grass",
    version="0.1",
    description="GRASS GIS Python's CFFI",
    long_description=open("README.rst", "rt").read(),
    url="https://github.com/zarch/python-cffi-grass",
    author="Pietro Zambelli",
    author_email="peter.zamb@gmail.com",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: PyPy",
        "License :: OSI Approved :: GPLv3",
    ],
    packages=find_packages(),
    install_requires=["cffi>=1.0.0"],
    setup_requires=["cffi>=1.0.0"],
    cffi_modules=[
        "./cffi_grass/build_grass.py:ffi",
    ],
)
