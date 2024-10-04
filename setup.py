from setuptools import setup, find_packages

# Reading the requirements.txt file
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='ds-and-algorithm',
    version='0.1',
    packages=find_packages(),
    install_requires=requirements,
)