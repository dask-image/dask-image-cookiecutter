#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import

{%- if cookiecutter.command_line_interface|lower == 'click' %}
from click.testing import CliRunner
from {{ cookiecutter.project_import }} import cli
{%- endif %}

import pytest


def test_import_core():
    try:
        from {{ cookiecutter.project_import }} import core
    except ImportError:
        pytest.fail("Unable to import `core`.")


{%- if cookiecutter.command_line_interface|lower == 'click' %}
def test_command_line_interface():
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert '{{ cookiecutter.project_import }}.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output

{%- endif %}
