from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='spalla',
   version='1.3',
   description='programma per verifiche Liceo Ariosto Spallanzani',
   license="MIT",
   long_description=long_description,
   author='Giovanni Bruno',
   author_email='br1giova@gmail.com',
   packages=['spalla'],
   install_requires=['requests'],
)
