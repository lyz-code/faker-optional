"""Test the command line interface."""

import logging
import re

import pytest
from _pytest.logging import LogCaptureFixture
from click.testing import CliRunner
from py._path.local import LocalPath
from faker_optional.config import Config
from faker_optional.entrypoints.cli import cli
from faker_optional.version import __version__


log = logging.getLogger(__name__)


@pytest.fixture(name="runner")
def fixture_runner() -> CliRunner:
    """Configure the Click cli test runner."""
    return CliRunner(mix_stderr=False)


def test_version(runner: CliRunner) -> None:
    """Prints program version when called with --version."""
    result = runner.invoke(cli, ["--version"])

    assert result.exit_code == 0
    assert re.match(
        fr" *faker_optional version: {__version__}\n"
        r" *python version: .*\n *platform: .*",
        result.stdout,
    )
