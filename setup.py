# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version='0.1.0',
    description='This is a smple project to be used as a template, yo',
    long_description=readme,
    author='Jon Gullotti',
    author_email='jgullotti@gmail.com',
    url='https://github.com/jgullotti/samplemod',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

