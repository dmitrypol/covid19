import pytest
import vcr
from app import APP, cli

RUNNER = APP.test_cli_runner()
#   https://flask.palletsprojects.com/en/1.1.x/testing/#testing-cli-commands


@vcr.use_cassette('tests/fixtures/vcr_cassettes/import_data.yml')
def test_import_data():
    result = RUNNER.invoke(cli.import_data, ['--date', APP.config.get('START_DATE')])
    assert f"imported for {APP.config.get('START_DATE')}" in result.output
