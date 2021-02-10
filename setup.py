from setuptools import setup
from setuptools import find_packages

with open('requirements.txt') as f:
    content = f.readlines()

install_requirements = [x.strip() for x in content]

setup(name="visinfo",
      description="package description",
      packages=find_packages(),
      install_requires=install_requirements)