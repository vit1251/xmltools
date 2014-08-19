#!/usr/bin/python

from setuptools import setup

setup(
    name="xmltool",
    version="0.1",
    author="Vitold Sedyshev",
    author_email="vit1251@gmail.com",
    description="XML Analytics Tool",
    keywords="xml agregate group",
    packages=['xmltool'],
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'xmltool = xmltool.stat:main',
        ],
    },
)
