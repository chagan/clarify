#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='Clarify',
    version='0.1.0',
    author='OpenElections',
    author_email='openelections@gmail.com',
    url='http://openelections.net',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests',
        'lxml',
        'cssselect',
        'six',
        'python-dateutil',
        'requests-futures',
    ],
    tests_require=[
        'nose',
        'responses',
    ],
    test_suite='nose.collector',
)
