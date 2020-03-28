''' command line tasks '''
# pylint: disable = missing-function-docstring, unused-argument, no-member, subprocess-run-check
import subprocess
import click
# from flask.cli import AppGroup
from . import APP

# APPG = AppGroup('foo')
# APP.cli.add_command(APPG)

@APP.cli.command()
def test():
    subprocess.run('APP_ENV=test pytest tests/* --cov=app && coverage html', shell=True)
    click.echo(click.style('test', bold=True, fg='blue'))
