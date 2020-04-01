''' command line tasks '''
# pylint: disable = unused-argument, no-member, subprocess-run-check
import subprocess
import click
# from flask.cli import AppGroup
from . import APP, scheduler, jobs, services

# APPG = AppGroup('foo')
# APP.cli.add_command(APPG)


@APP.cli.command()
def test():
    subprocess.run('APP_ENV=test pytest tests/* --cov=app && coverage html', shell=True)
    click.echo(click.style('test completed', bold=True, fg='blue'))


@APP.cli.command()
def sched_start():
    scheduler.SCHED.start()


@APP.cli.command()
@click.option('-d', '--date', required=True, help=APP.config.get('START_DATE'))
def import_data(date):
    jobs.import_data(date)
    click.echo(click.style(f'imported for {date}', bold=True, fg='blue'))


@APP.cli.command()
def reimport_data():
    for date in services.get_import_dates_list():
        jobs.import_data.queue(date)
        click.echo(click.style(f'queued import for {date}', fg='red'))
    click.echo(click.style(f'completed queueing', bold=True, fg='blue'))
