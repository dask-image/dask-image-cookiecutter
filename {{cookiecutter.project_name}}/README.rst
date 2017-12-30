{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
{% for _ in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

{% if is_open_source %}
.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.project_name }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.project_name }}
        :alt: PyPI

.. image:: https://img.shields.io/conda/vn/conda-forge/{{ cookiecutter.project_name }}.svg
        :target: https://anaconda.org/conda-forge/{{ cookiecutter.project_name }}
        :alt: conda-forge

.. image:: https://img.shields.io/travis/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}/master.svg
        :target: https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}
        :alt: Travis CI

.. image:: https://readthedocs.org/projects/{{ cookiecutter.project_name | replace("_", "-") }}/badge/?version=latest
        :target: https://{{ cookiecutter.project_name | replace("_", "-") }}.readthedocs.io/en/latest/?badge=latest
        :alt: Read the Docs

.. image:: https://coveralls.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}/badge.svg
        :target: https://coveralls.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}
        :alt: Coveralls

.. image:: https://img.shields.io/github/license/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}.svg
        :target: ./LICENSE.txt
        :alt: License
{%- endif %}


{{ cookiecutter.project_short_description }}

{% if is_open_source %}
* Free software: {{ cookiecutter.open_source_license }}
* Documentation: https://{{ cookiecutter.project_name | replace("_", "-") }}.readthedocs.io.
{% endif %}

Features
--------

* TODO

Credits
---------

This package was created with Cookiecutter_ and the `dask-image/dask-image-cookiecutter`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`dask-image/dask-image-cookiecutter`: https://github.com/dask-image/dask-image-cookiecutter

