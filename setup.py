# Copyright 2022, Ryan P. Kelly.

from setuptools import setup


setup(
    name="eruza",
    version="0.3",
    description="Azure + CLI",
    author="Ryan P. Kelly",
    author_email="ryan@ryankelly.us",
    url="https://github.com/f0rk/eruza",
    tests_require=[
        "pytest",
    ],
    package_dir={"": "lib"},
    packages=["eruza"],
    scripts=["tools/eruza"],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3",
        "Topic :: System :: Systems Administration",
    ],
)
