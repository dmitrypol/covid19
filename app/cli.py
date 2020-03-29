''' command line tasks '''
# pylint: disable = unused-argument, no-member, subprocess-run-check
import subprocess
import click
# from flask.cli import AppGroup
from . import APP, scheduler, jobs

# APPG = AppGroup('foo')
# APP.cli.add_command(APPG)


@APP.cli.command()
def test():
    subprocess.run('APP_ENV=test pytest tests/* --cov=app && coverage html', shell=True)
    click.echo(click.style('test', bold=True, fg='blue'))


@APP.cli.command()
def sched_start():
    scheduler.SCHED.start()


@APP.cli.command()
@click.option('-d', '--date', required=True, help='03-22-2020')
def import_data(date):
    jobs.import_data(date)
    click.echo(click.style(f'imported for {date}', bold=True, fg='blue'))
