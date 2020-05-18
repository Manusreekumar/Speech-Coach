# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Speech-Coach',
    version='0.1.0',
    description='Machine learning application for reporting energy levels of speech audio',
    long_description=readme,
    author='Manu Sreekumar',
    author_email='manusreekumar04@gmail.com',
    url='https://github.com/Manusreekumar/Speech-Coach.git',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

