from glob import glob
from os.path import basename, splitext
from setuptools import find_packages, setup

setup(
    name='FinanceDataReader',
    url='https://github.com/melemo2/FinanceDataReader.git',
    version='0.1',
    packages=find_packages(),
    license='MIT',
    install_requires=[],
    zip_safe=False,
)