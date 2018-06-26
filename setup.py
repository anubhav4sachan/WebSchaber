# -*- coding: utf-8 -*-

import setuptools

try:
    README = open('README.md').read()
except:
    README = '"README.md" not found'

VERSION = '1.0'
NAME = 'webschaber'
SHORT_DESC = 'The WebSchaber is python3 script which extracts the text and images content on search engine `bing.com`'
AUTHOR = 'Anubhav Sachan'
EMAIL = 'anubhav4sachan@gmail.com'
LICENSE = 'GNU GPL v3'
URL = 'https://www.github.com/anubhav4sachan/WebSchaber'
PKG = ['webschaber']

setuptools.setup(
        name = NAME,
        version = VERSION,
        description = SHORT_DESC,
        long_description = README,
        url = URL,
        author = AUTHOR,
        author_email = EMAIL,
        packages = PKG
)