======================
Cookiecutter PyPackage
======================

This package contains a `Cookiecutter`_ template for a Python package.
It implements my preferred style guidelines, and automates the setup of test suites, CLI interfaces, CI/CD pipelines, and documentation.

Usage
-----

To use this template, you need to have `Cookiecutter`_ installed. If you don't have it installed, you can install it using pip:

.. code-block:: bash

    $ pip install cookiecutter


To use pre-commit hooks which ensure code compliance before allowing commits (as is default), you also need to install `pre-commit`_:

.. code-block:: bash

    $ pip install pre-commit


Afterwards, you can generate a new Python package using this template by running the following command:

.. code-block:: bash

    $ cookiecutter git@github.com:LokiLuciferase/cookiecutter-pypackage.git


This will prompt you to enter some information about your package, such as the package name, author name, and license. After providing the required information, `Cookiecutter`_ will generate a new directory with the project structure and files for your Python package.


Documentation
-------------

.. _Cookiecutter: https://cookiecutter.readthedocs.io/
.. _pre-commit: https://pre-commit.com/
.. _Cookiecutter PyPackage Documentation: https://github.com/LokiLuciferase/cookiecutter-pypackage/blob/main/docs/index.rst
