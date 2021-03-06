"""
alchy
=====

The declarative companion to SQLAlchemy.

Documentation: http://dgilland.github.io/alchy

Project: https://github.com/dgilland/alchy
"""

from setuptools import setup

setup(
    name='alchy',
    version='0.6.0',
    url='https://github.com/dgilland/alchy',
    license='MIT',
    author='Derrick Gilland',
    author_email='dgilland@gmail.com',
    description='SQLAlchemy enhancement library.',
    long_description=__doc__,
    packages=['alchy'],
    install_requires=[
        'SQLAlchemy>=0.9.0',
        'six'
    ],
    test_suite='tests',
    keywords='sqlalchemy databases',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Topic :: Database :: Front-Ends',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
    ]
)
