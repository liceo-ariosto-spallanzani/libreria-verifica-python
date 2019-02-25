from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='verifica',
   version='0.1',
   description='A useful module',
   license="MIT",
   long_description=long_description,
   author='Man Foo',
   author_email='br1gioca@gmail.com',
   packages=['verifica'],
   install_requires=['requests'],
)