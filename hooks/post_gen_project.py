#!/usr/bin/env python
import os
from subprocess import call, DEVNULL

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':

    if '{{ cookiecutter.detailed_contribution_info }}' != 'y':
        remove_file('AUTHORS.rst')
        remove_file('CONTRIBUTING.rst')
        remove_file('HISTORY.rst')
        remove_file('docs/authors.rst')
        remove_file('docs/history.rst')
        remove_file('docs/contributing.rst')

    if '{{ cookiecutter.ci_strategy }}'.lower() != 'travis':
        remove_file('.travis.yml')
    if '{{ cookiecutter.ci_strategy }}'.lower() != 'github':
        remove_file('.github/workflows/ci.yml')
        remove_file('.github/workflows/docs.yml')
    if '{{ cookiecutter.ci_strategy }}'.lower() != 'bitbucket':
        remove_file('bitbucket-pipelines.yml')

    if '{{ cookiecutter.use_precommit }}' != 'y':
        remove_file('.pre-commit-config.yaml')

    if '{{ cookiecutter.use_docker }}' != 'y':
        remove_file('Dockerfile')

    if 'no' in '{{ cookiecutter.command_line_interface|lower }}':
        cli_file = os.path.join('{{ cookiecutter.project_slug }}', 'cli.py')
        remove_file(cli_file)

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')

    print('Setting up git.')
    call(['git', 'init'], stderr=DEVNULL, stdout=DEVNULL)
    call(['git', 'add', '*'], stderr=DEVNULL, stdout=DEVNULL)
    call(['git', 'commit', '-m', 'Initial commit'], stderr=DEVNULL, stdout=DEVNULL)
    if '{{ cookiecutter.use_precommit }}' == 'y':
        print('Setting up pre-commit.')
        try:
            call(['pre-commit', 'install'])
        except FileNotFoundError:
            print('To install pre-commit hooks, run "pre-commit install" in the newly created project.')

