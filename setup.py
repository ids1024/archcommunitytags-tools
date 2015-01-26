#!/usr/bin/env python3

from distutils.core import setup

setup(name='communitytags',
      version='0.1',
      description='Community provided tags for packages.',
      author='Ian D. Scott',
      author_email='ian@perebruin.com',
      license = "GPL3",
      url='http://github.com/ids1024/archcommunitytags-tools/',
      data_files=[
          ('/usr/share/man/man1', ['communitytags.1']),
          ],
      scripts = ['communitytags'],
     )
