from setuptools import setup, find_packages

import djm_sdk

setup(
    name=djm_sdk.__package__,
    version=djm_sdk.__version__,
    description=('Dejamobile Take Home - Backend API SDK'),
    author='Antoine BUHOT',
    author_mail='buhot.a@gmail.com',
    license='MIT',
    packages=find_packages(exclude=['unit_tests',]),
    install_requires=[

    ]
)