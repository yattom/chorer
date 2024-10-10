from pytest import fixture
from click.testing import CliRunner

from chorer.main import bare_web as cmd
from chorer.commands.bare_web.bare_web import bare_web


@fixture
def runner():
    return CliRunner()

def test_help(runner):
    result = runner.invoke(cmd, ['--help'])
    assert result.exit_code == 0
    assert 'build bare web application' in result.output


def test_output_structure(runner, tmp_path):
    result = bare_web(tmp_path.absolute(), 'apptest')
    assert (tmp_path / 'apptest' / 'backend').is_dir()
    assert (tmp_path / 'apptest' / 'frontend').is_dir()
    assert (tmp_path / 'apptest' / 'frontend' / 'package.json').is_file()
