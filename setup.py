# -*- coding: utf-8 -*-
"""
For installing the hdf2mic package with setuptools to a Python env.
"""

from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='hdf2mic',
      version='1.0',
      description='Convert DREAM3D HDF5 synthetic microstructure file'
                  'to MICRESS input files TXT and ASCII VTK',
      classifiers=[
          'License :: MIT',
          'Programming Language :: Python :: 3.11',
          'Topic :: Scientific/Engineering :: Interface Engine/Protocol Translator',
      ],
      url='https://git.gi.rwth-aachen.de/micress-utils/hdf2mic.git',
      author='Johannes Wasmer, Ralph Altenfeld',
      author_email='r.altenfeld@access-technology.de',
      license='MIT',
      python = ">=3.0",
      packages=['hdf2mic'],
      install_requires=[
          'numpy',
          'h5py'
      ],
      scripts=['hdf2mic.py'],
      zip_safe=False)