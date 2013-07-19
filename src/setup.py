#!/usr/bin/env python

from distutils.core import setup

setup(name='pyldap',
      version='1.0.0.0',
      description='Python Ldap Auth',
      long_description='The ldap authentication component',
      author='Michel Antunes',
      author_email='michelantunesdasilva@gmail.com',
      maintainer='Michel Antunes',
      maintainer_email='michelantunesdasilva@gmail.com',
      url='http://github.com/michelantunes/pyldap',
      download_url='http://github.com/michelantunes/pyldap/src/dist/',
      packages=['pyldap','pyldap.control'],
      package_dir={'pyldap': 'pyldap','pyldap.control': 'pyldap/control'},
      classifiers={},
     )