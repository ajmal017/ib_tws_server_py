from setuptools import setup

import sys

if sys.version_info < (3,9):
    sys.exit("Only Python 3.9 and greater is supported") 

setup(
    name='ib_tws_server',
    version="0.0.0",
    packages=['ib_tws_server'],
    url='https://interactivebrokers.github.io/tws-api',
    license='IB API Non-Commercial License or the IB API Commercial License',
    author='Chandra Penke',
    author_email='dnastase@interactivebrokers.com',
    description='Python IB API'
)
