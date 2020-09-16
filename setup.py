#!/usr/bin/env python

import os.path
import sys

from setuptools import setup, find_packages

import django_states

sys.path.insert(0, os.path.dirname(__file__))


setup(
    name="django-states",
    version=django_states.__version__,
    url='https://github.com/citylive/django-states2',
    license='BSD',
    description="State machine for django models",
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    author='Jonathan Slenders, Gert van Gool, Maarten Timmerman, Steven (rh0dium)',
    author_email='jonathan.slenders@mobilevikings.com',
    packages=find_packages('.', exclude=['test_proj',]),
    python_requires=">=3.5",
    install_requires=[
        "six"
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
    ],
)
