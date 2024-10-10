from pytest import fixture
from click.testing import CliRunner

from chorer.main import bare_web
from chorer.commands.bare_web import invoke


@fixture
def runner():
    return CliRunner()

def test_help(runner):
    result = runner.invoke(bare_web, ['--help'])
    assert result.exit_code == 0
    assert 'build bare web application' in result.output


def test_output_structure(runner, tmp_path):
    result = invoke(tmp_path.absolute(), 'apptest')
    assert (tmp_path / 'apptest' / 'backend').is_dir()
    assert (tmp_path / 'apptest' / 'frontend').is_dir()
    assert (tmp_path / 'apptest' / 'frontend' / 'package.json').is_file()
    assert (tmp_path / 'apptest' / 'frontend' / 'node_packages').is_dir()

