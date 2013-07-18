#!/usr/bin/env python

from distutils.core import setup

setup(name='pyldap',
      version='1.0',
      description='Python Ldap Auth',
      author='Michel Antunes',
      author_email='michelantunesdasilva@gmail.com',
      url='http://github.com/michelantunes/pyldap',
      packages=['pyldap','pyldap.control'],
      package_dir={'pyldap': 'pyldap','pyldap.control': 'pyldap/control'},
     )