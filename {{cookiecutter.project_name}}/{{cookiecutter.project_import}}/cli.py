# -*- coding: utf-8 -*-

import click


@click.command()
def main(args=None):
    """Console script for {{cookiecutter.project_import}}"""
    click.echo("Replace this message by putting your code into "
               "{{cookiecutter.project_import}}.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")


if __name__ == "__main__":
    main()
