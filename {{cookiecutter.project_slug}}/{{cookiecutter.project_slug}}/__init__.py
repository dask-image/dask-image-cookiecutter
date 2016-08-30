# -*- coding: utf-8 -*-

__author__ = '{{ cookiecutter.full_name }}'
__email__ = '{{ cookiecutter.email }}'

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
