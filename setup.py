# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 13:59:52 2019

@author: Joshua E. Lambert
"""

from setuptools import setup, find_packages
import os

module_dir = os.path.dirname(os.path.abspath(__file__))

setup(
    name='sswebdata',
    version='0.0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='A package to to pull data from open sources on the web related to Security Studies',
    long_description=open(os.path.join(module_dir, 'README.md')).read(),
    install_requires=[],
    url='https://github.com/JELambert/sswebdata',
    author=['Joshua E. Lambert'],
    author_email=['joshua.lambert@knights.ucf.edu']
)
