# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='diplodatos',
    version='0.1.0',
    description='Course repository',
    long_description=readme,
    author='Adrian Tissera',
    author_email='adriantissera@gmail.com',
    url='https://github.com/dahue/diplodatos',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
