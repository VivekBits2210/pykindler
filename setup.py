import setuptools
from os import path
from pykindler import cli

thelibFolder = path.dirname(path.realpath(__file__))
requirementPath = thelibFolder + '/requirements.txt'
install_requires = []
if path.isfile(requirementPath):
    with open(requirementPath) as f:
        install_requires = f.read().splitlines()

setuptools.setup(
	name='pykindler',
	install_requires=install_requires,
	version='0.1',
	description="Schedules conversion of e-books to mobi, mails it to your kindle",
	long_description="Schedules conversion of e-books to mobi, mails it to your kindle (repo: https://github.com/VivekBits2210/pykindler)",
	entry_points={
        'console_scripts': [
            'pykindler-run=pykindler.cli:main'
        ]
    },
	packages=setuptools.find_packages()
)
