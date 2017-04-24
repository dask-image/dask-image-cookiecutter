Welcome to {{ cookiecutter.project_name }}'s documentation!
======================================

Contents:

.. toctree::
   :maxdepth: 1

   Readme <readme>
   installation
   usage
   api
   contributing
   {% if cookiecutter.create_author_file == 'y' -%}
   authors
   {% endif -%}
   history

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
