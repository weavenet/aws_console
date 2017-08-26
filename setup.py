#!/usr/bin/env python

from distutils.core import setup

setup(name='aws_console',
      version='1.0',
      description='Generate signed AWS console urls',
      author='Brett Weaver',
      author_email='',
      url='https://github.com/weavenet/aws_console',
      packages=['aws_console'],
      install_requires=['boto3', 'requests'],
      entry_points = {
          'console_scripts': [
              'console_via_env_variables = aws_console.console_via_env_variables:run',
              'console_via_assume_role = aws_console.console_via_assume_role:run'
              ]
          }
     )
