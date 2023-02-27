Prompts
=======

When you create a package, you are prompted to enter these values.

Templated Values
----------------

The following appear in various parts of your generated project.

full_name
    Your full name.

email
    Your email address.

github_username
    Your GitHub username.

project_name
    The name of your new Python package project. This is used in documentation, so spaces and any characters are fine here.

project_slug
    The namespace of your Python package. This should be Python import-friendly. Typically, it is the slugified version of project_name.

project_short_description
    A 1-sentence description of what your Python package does.

release_date
    The date of the first release.

pypi_username
    Your Python Package Index account username.

year
    The year of the initial package copyright in the license file.

version
    The starting version number of the package.

Options
-------

The following package configuration options set up different features for your project.

use_strict_typing
    Whether to use strict type checking (statically with `mypy <http://mypy-lang.org/>`_ during pre_commit, dynamically during testing with `typeguard <https://typeguard.readthedocs.io/>`_)

use_precommit
    Whether to install a comprehensive set of `pre-commit <https://pre-commit.com/>`_ hooks to automatically perform code reformatting previous to commits and pushes.

use_docker
    Whether to include a `Dockerfile <https://docs.docker.com/engine/reference/builder/>`_ for the project

add_pyup_badge
    Whether to include a `pyup <https://github.com/pyupio/pyup>`_ badge

command_line_interface
    Whether to create a console script using Click. Console script entry point will match the project_slug. Options: ['Click', 'Argparse', 'No command-line interface']

detailed_contribution_info
    Whether to create an authors file, a history file and a contributing file for the project

open_source_license
    Choose a `license <https://choosealicense.com/>`_. Options: [1. MIT License, 2. BSD license, 3. ISC license, 4. Apache Software License 2.0, 5. GNU General Public License v3, 6. Not open source]
