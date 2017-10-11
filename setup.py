#!/usr/bin/env python

from distutils.core import setup

setup(name='aws_console',
      version='1.0.1',
      description='Generate signed AWS console urls',
      author='Brett Weaver',
      author_email='',
      url='https://github.com/weavenet/aws_console',
      packages=['aws_console'],
      install_requires=['boto3', 'requests'],
      entry_points = {
          'console_scripts': [
              'aws_console = aws_console.cli:run'
              ]
          }
     )
