#!/usr/bin/env python
from distutils.core import setup

setup(name='pushover',
      version='1.2',
      description='Pushover Notify',
      author='yoloClin',
      author_email='yoloClin@github.com',
      url='https://github.com/yoloClin/python-pushover',
      packages=['pushover'],
      package_dir={"pushover": "pushover"},
      scripts=['bin/pushover-notify', 'bin/wheres-my-phone',
               'bin/wheres-my-phone-nice-mode']
      )
