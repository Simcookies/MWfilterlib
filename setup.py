from setuptools import setup, find_packages
from os import path

setup(
    name = "MWfilterlib",
    version = "0.0.1",
    keywords = 'microwave filter',
    description = "a library for cal params from known model.",
    license = "MIT License",
    url = "https://github.com/Simcookies/MWfilterlib",
    author = "An Song",
    author_email = "songan840136@gmail.com",
    packages = find_packages(),
    include_package_data = True,
    install_requires = [],
)
