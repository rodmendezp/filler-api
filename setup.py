from setuptools import setup, find_packages

setup(name='fillerapi',
      version='0.13',
      description='API Client for Filler',
      author='Rodrigo Mendez',
      author_email='rodmendezp@gmail.com',
      packages=find_packages(),
      zip_safe=False, install_requires=['requests', 'djangorestframework'])
