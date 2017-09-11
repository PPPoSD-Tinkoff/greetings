#!/usr/bin/env python3

"""Setup script."""

from setuptools import setup

setup(
    name="greetings",
    version="0.0.0",
    author="Arthur Khashaev",
    author_email="arthur@khashaev.ru",
    url="https://github.com/PPPoSD-2017/greetings",
    license="MIT",
    packages=[
        "greetings",
    ],
    install_requires=[
    ],
    setup_requires=[
        "pytest-runner",
        "pytest-pylint",
        "pytest-pycodestyle",
        "pytest-pep257",
    ],
    tests_require=[
        "pytest",
        "pylint",
        "pycodestyle",
        "pep257",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ]
)
