import logging

from kaon import logger
from kaon.cli import main


def test_verbosity(app_env, db, cli):
    app_dir, config_path, tmp_path = app_env

    result = cli.invoke(main, ["--version"])
    assert result.exception is None
    assert result.exit_code == 0
    assert logger.logger.getEffectiveLevel() == logging.WARNING
    assert logging.getLogger().getEffectiveLevel() == logging.WARNING

    result = cli.invoke(main, ["--version", "-v"])
    assert result.exit_code == 0
    assert result.exception is None
    assert logger.logger.getEffectiveLevel() == logging.INFO
    assert logging.getLogger().getEffectiveLevel() == logging.INFO

    result = cli.invoke(main, ["--version", "-vv"])
    assert result.exit_code == 0
    assert result.exception is None
    assert logger.logger.getEffectiveLevel() == logging.DEBUG
    assert logging.getLogger().getEffectiveLevel() == logging.INFO

    result = cli.invoke(main, ["--version", "-vvv"])
    assert result.exit_code == 0
    assert result.exception is None
    assert logger.logger.getEffectiveLevel() == logging.DEBUG
    assert logging.getLogger().getEffectiveLevel() == logging.DEBUG
