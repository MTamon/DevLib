# -*- coding: utf-8 -*-

from os import path
from setuptools import setup

# TODO: change project to your project name
from project import VERSION, LICENCE, AUTHOR, EMAIL, GIT_URL

NAME = "project"
PACKAGES = ["project"]
DESCRIPTION = "description"
KEYWORDS = "keywords1, kyewords2, keywords3, ..."

root_dir = path.abspath(path.dirname(__file__))


def _requirements():
    return [
        name.rstrip()
        for name in open(
            path.join(root_dir, "requirements.txt"), encoding="utf-8"
        ).readlines()
    ]


def _test_requirements():
    return [
        name.rstrip()
        for name in open(
            path.join(root_dir, "test-requirements.txt"), encoding="utf-8"
        ).readlines()
    ]


assert VERSION
assert LICENCE
assert AUTHOR
assert EMAIL
assert GIT_URL

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()


setup(
    name=NAME,
    packages=PACKAGES,
    version=VERSION,
    license=LICENCE,
    install_requires=_requirements(),
    tests_require=_test_requirements(),
    author=AUTHOR,
    author_email=EMAIL,
    url=GIT_URL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=KEYWORDS,
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
