Welcome to {{ cookiecutter.project_name }}'s documentation!
==========={% for _ in cookiecutter.project_name %}={% endfor %}=================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   readme
   installation
   usage
   {% if cookiecutter.detailed_contribution_info == 'y' -%}authors
   contributing
   history
   {% endif -%}modules


Indices and tables
==================
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
