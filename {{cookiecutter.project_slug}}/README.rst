{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
===============================
{{ cookiecutter.project_name }}
===============================

{% if is_open_source %}
.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}

.. image:: https://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.svg
        :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}

.. image:: https://readthedocs.org/projects/{{ cookiecutter.project_slug | replace("_", "-") }}/badge/?version=latest
        :target: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://coveralls.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/badge.svg
        :target: https://coveralls.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
        :alt: Coveralls

.. image:: https://img.shields.io/github/license/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.svg
        :target: ./LICENSE.txt
        :alt: License
{%- endif %}


{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* Free software: {{ cookiecutter.open_source_license }}
* Documentation: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io.
{% endif %}

Features
--------

* TODO

Credits
---------

This package was created with Cookiecutter_ and the `nanshe-org/nanshe-cookiecutter`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`nanshe-org/nanshe-cookiecutter`: https://github.com/nanshe-org/nanshe-cookiecutter

