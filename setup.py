#!/usr/bin/env python

# This will try to import setuptools. If not here, it will reach for the embedded
# ez_setup (or the ez_setup package). If none, it fails with a message
try:
    from setuptools import setup
except ImportError:
    try:
        import ez_setup
        ez_setup.use_setuptools()
    except ImportError:
        raise ImportError("hachoir-metadata extracts metadata from multimedia files: "
                          "music, picture, video, but also archives.")

from setuptools import setup, find_packages

setup(name='hachoir_metadata',
      version='1.3.3',
      author='Victor Stinner',
      description='Program to extract metadata using Hachoir library',
      long_description=open('README.rst').read(),
      url='https://github.com/eduardoburgoa/hachoir_metadata',
      license='GNU GPL v2',
      keywords="file binary metadata",
      packages=find_packages(exclude='docs'),
      install_requires=[])
