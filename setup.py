#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='horizon_dashboard_boilerplate',
    version='0.1.0',
    description="Openstack Horizon pluggable dashboard boilerplate, provides basicc foundation of dashboard and panels.",
    long_description=readme + '\n\n' + history,
    author="Arslan Rafique",
    author_email='mailtoarslan@gmail.com',
    url='https://github.com/arslanrafique/horizon_dashboard_boilerplate',
    packages=[
        'horizon_dashboard_boilerplate',
        'horizon_dashboard_boilerplate/boilerplate_panel',
        'horizon_dashboard_boilerplate/boilerplate_panel/templates/boilerplate_panel'
    ],
    package_dir={'horizon_dashboard_boilerplate':
                 'horizon_dashboard_boilerplate'},
    include_package_data=True,
    install_requires=requirements,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords='horizon_dashboard_boilerplate',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
