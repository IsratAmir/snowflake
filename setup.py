from distutils.core import setup
from setuptools import find_packages

setup(
    name="Snowflake",
    version ="0.1",
    author="Israt Amir",
    author_email="isratamir.aust@gmail.com",
    packages=find_packages(),
    install_requires= ["numpy", "turtles"]
)