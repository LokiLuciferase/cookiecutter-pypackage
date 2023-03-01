Tutorial
========

.. note:: Did you find any of these instructions confusing? `Edit this file`_
          and submit a pull request with your improvements!

.. _`Edit this file`: https://github.com/LokiLuciferase/cookiecutter-pypackage/blob/master/docs/tutorial.rst

To start with, you will need a `GitHub account`_ and an account on `PyPI`_. Create these before you get started on this tutorial. If you are new to Git and GitHub, you should probably spend a few minutes on some of the tutorials at the top of the page at `GitHub Help`_.

.. _`GitHub account`: https://github.com/
.. _`PyPI`: https://pypi.python.org/pypi
.. _`GitHub Help`: https://help.github.com/


Step 1: Install Cookiecutter
----------------------------

First, you need to create and activate a virtualenv for the package project. Use your favorite method, or create a virtualenv for your new package like this:

.. code-block:: bash

    virtualenv ~/.virtualenvs/mypackage

Here, ``mypackage`` is the name of the package that you'll create.

Activate your environment:

.. code-block:: bash

    source bin/activate

On Windows, activate it like this. You may find that using a Command Prompt window works better than gitbash.

.. code-block:: powershell

    > \path\to\env\Scripts\activate


Install cookiecutter:

.. code-block:: bash

    pip install cookiecutter


Step 2: Generate Your Package
-----------------------------

Now it's time to generate your Python package.

Use cookiecutter, pointing it at the cookiecutter-pypackage repo:

.. code-block:: bash

    cookiecutter https://github.com/LokiLuciferase/cookiecutter-pypackage.git

You'll be asked to enter a bunch of values to set the package up.
If you don't know what to enter, stick with the defaults.


Step 3: Create a GitHub Repo
----------------------------

Go to your GitHub account and create a new repo named ``mypackage``, where ``mypackage`` matches the ``[project_slug]`` from your answers to running cookiecutter.

``If your virtualenv folder is within your project folder, be sure to add the virtualenv folder name to your .gitignore file.``

You will find one folder named after the ``[project_slug]``. Move into this folder, and then setup git to use your GitHub repo and upload the code:

.. code-block:: bash

    cd mypackage
    git init .
    git add .
    git commit -m "Initial skeleton."
    git remote add origin git@github.com:myusername/mypackage.git
    git push -u origin master

Where ``myusername`` and ``mypackage`` are adjusted for your username and package name.

You'll need a ssh key to push the repo. You can `Generate`_ a key or `Add`_ an existing one.

.. _`Generate`: https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/
.. _`Add`: https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/


Step 4: Install Dev Requirements
--------------------------------

Your virtualenv should still be activated. If it isn't, activate it now. Install the new project's local development requirements:

.. code-block:: bash

    make install_dev


Step 7: Release on PyPI
-----------------------

The Python Package Index or `PyPI`_ is the official third-party software repository for the Python programming language. Python developers intend it to be a comprehensive catalog of all open source Python packages.

When you are ready, release your package the standard Python way.

See `PyPI Help`_ for more information about submitting a package.

.. _`PyPI`: https://pypi.python.org/pypi
.. _`PyPI Help`: http://peterdowns.com/posts/first-time-with-pypi.html


Having problems?
----------------

Visit our :ref:`troubleshooting` page for help. If that doesn't help, go to our `Issues`_ page and create a new Issue. Be sure to give as much information as possible.

.. _`Issues`: https://github.com/LokiLuciferase/cookiecutter-pypackage/issues
