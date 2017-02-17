import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
setup(
    # Application name:
    name="MedicalHistory",

    # Version number (initial):
    version="0.1.0",

    # Application author details:
    author="veronica prado",
    author_email="pradovc01@gmail.com",

    # Packages
    packages=find_packages(),

    # Include additional files into the package
    include_package_data=True,

    #
    license="LICENSE.txt",
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)