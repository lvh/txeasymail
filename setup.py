#!/usr/bin/env python
from setuptools import find_packages, setup

setup(name='txeasymail',
      version='20121010',
      description='Twisted client for easy email sending',
      url='https://github.com/lvh/txeasymail',

      author='Laurens Van Houtven',
      author_email='_@lvh.cc',

      packages=find_packages(),

      install_requires=['twisted'],

      license='ISC',
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Twisted",
        "License :: OSI Approved :: ISC License (ISCL)",
        ])
