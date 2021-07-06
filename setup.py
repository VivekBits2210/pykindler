__author__ = "Vivek Nayak"

import setuptools
from os import path
from pykindler import cli

try:
    # Used to convert md to rst for pypi, otherwise not needed
    import m2r
except ImportError:
    m2r = None

thelibFolder = path.dirname(path.realpath(__file__))
requirementPath = thelibFolder + "/requirements.txt"
install_requires = []
if path.isfile(requirementPath):
    with open(requirementPath) as f:
        install_requires = f.read().splitlines()

description = "Schedules conversion of e-books to mobi, mails it to your kindle"
if m2r is None:
    long_description = description
else:
    # convert markdown to rst
    long_description = m2r.convert(open("README.md").read())

setuptools.setup(
    name="pykindler",
    install_requires=install_requires,
    version="0.3.2",
    description=description,
    long_description=long_description,
    license="MIT",
    author="Vivek Nayak",
    author_email="viveknayak2210@gmail.com",
    url="https://github.com/VivekBits2210/pykindler",
    entry_points={"console_scripts": ["pykindler-run=pykindler.cli:client"]},
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Intended Audience :: End Users/Desktop",
        "Environment :: Console",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "License :: OSI Approved :: MIT License",
        "Topic :: Utilities",
    ],
)
