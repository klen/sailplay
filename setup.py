#!/usr/bin/env python

import re
import sys
from os import path as op

from setuptools import setup
from setuptools.command.test import test as TestCommand


def _read(fname):
    try:
        return open(op.join(op.dirname(__file__), fname)).read()
    except IOError:
        return ''

_meta = _read('sailplay.py')
_license = re.search(r'^__license__\s*=\s*"(.*)"', _meta, re.M).group(1)
_project = re.search(r'^__project__\s*=\s*"(.*)"', _meta, re.M).group(1)
_version = re.search(r'^__version__\s*=\s*"(.*)"', _meta, re.M).group(1)

install_requires = [
    l for l in _read('requirements.txt').split('\n')
    if l and not l.startswith('#')]

tests_require = [
    l for l in _read('requirements-tests.txt').split('\n')
    if l and not l.startswith('#')]


class __PyTest(TestCommand):

    test_args = []
    test_suite = True

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    name=_project,
    version=_version,
    license=_license,
    description='API Client for sailplay.ru',
    long_description=_read('README.rst'),
    platforms=('Any'),
    keywords = "django flask sqlalchemy testing mock stub mongoengine data".split(), # noqa

    author='Kirill Klenov',
    author_email='horneds@gmail.com',
    url='https://github.com/klen/sailplay',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Natural Language :: Russian',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities',
    ],

    py_modules=['sailplay'],
    include_package_data=True,
    install_requires=install_requires,
    tests_require=tests_require,
    cmdclass={'test': __PyTest},
)

# pylama:ignore=D
