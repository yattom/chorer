from click.testing import CliRunner
from chorer.main import bare_web


def test_help():
    runner = CliRunner()
    result = runner.invoke(bare_web, ['--help'])
    assert result.exit_code == 0
    assert 'build bare web application' in result.output
