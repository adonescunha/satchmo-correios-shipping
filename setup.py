#!/usr/bin/env python
# -*- coding: utf-8 -*-

# satchmo-correios-shipping
# https://github.com/adonescunha/satchmo-correios-shipping

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2014 Adones Cunha adonescunha@gmail.com


__version__ = '0.1.2'

from setuptools import setup


setup(
    name='satchmo-correios-shipping',
    version=__version__,
    description='Utility classes and functions to use Correios as shipping method on Satchmo.',
    author='Adones Cunha',
    author_email='adonescunha@gmail.com',
    url='https://github.com/adonescunha/satchmo-correios-shipping',
    packages=[
        'satchmo_correios_shipping'
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        'Topic :: Software Development :: Testing'
    ],
    install_requires=[
        'correios-frete',
    ]
)
