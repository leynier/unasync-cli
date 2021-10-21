from typer.testing import CliRunner
from unasync_cli.main import app

runner = CliRunner()


def test_unasync_cli():
    assert runner.invoke(app, ["--help"]).exit_code == 0
