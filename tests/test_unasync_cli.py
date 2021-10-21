from typer.testing import CliRunner

from unasync_cli.main import app

runner = CliRunner()


def test_unasync_cli():
    result = runner.invoke(app)
    assert result.exit_code == 0
    assert "Hello World!" in result.stdout
