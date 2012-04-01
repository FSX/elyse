import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='elyse',
    version='0.1.0',
    description='A simple static website generator.',
    author='Frank Smit',
    author_email='frank@61924.nl',
    license='MIT',
    long_description=open('README.rst').read(),
    scripts=['elyse'],
    install_requires=[
        'pyyaml',
        'tornado',
        'houdini.py',
        'misaka',
        'pygments',
        'unidecode'
    ],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Topic :: Text Processing',
        'Topic :: Utilities'
    ]
)
