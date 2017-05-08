import re
import sys


PROJ_REGEX = r'^[_a-zA-Z][\-_a-zA-Z0-9]+$'
MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

proj_name = '{{ cookiecutter.project_name }}'
module_name = '{{ cookiecutter.project_import }}'


if not re.match(PROJ_REGEX, proj_name):
    print('ERROR: The project name (%s) is not a valid PyPI package name. Please do not use spaces.' % proj_name)

    #Exit to cancel project
    sys.exit(1)


if not re.match(MODULE_REGEX, module_name):
    print('ERROR: The project slug (%s) is not a valid Python module name. Please do not use a - and use _ instead.' % module_name)

    #Exit to cancel project
    sys.exit(1)
