import functools
import os

import pytest
from click.testing import CliRunner

import kaon
from kaon import model
from kaon.db import database


@pytest.yield_fixture
def db():
    database.init(":memory:")
    database.connect()
    database.create_tables([getattr(model, m) for m in model.__all__])
    yield database
    database.close()

@pytest.fixture
def app_env(tmp_path, monkeypatch):
    app_dir = os.path.join(tmp_path, "app")
    config_path = os.path.join(app_dir, "config.yml")
    monkeypatch.setattr("kaon.config.APP_DIR", app_dir)
    monkeypatch.setattr("kaon.config.CONFIG_FILE", config_path)
    monkeypatch.setattr("kaon.config.DB_FILE", os.path.join(app_dir, "database.sqlite"))
    assert not os.path.exists(config_path)
    assert kaon.config.APP_DIR == app_dir
    assert kaon.config.CONFIG_FILE == config_path
    return app_dir, config_path, tmp_path

@pytest.fixture
def cli():
    """Yield a click.testing.CliRunner to invoke the CLI."""
    class_ = CliRunner

    def invoke_wrapper(f):
        """Augment CliRunner.invoke to emit its output to stdout.

        This enables pytest to show the output in its logs on test
        failures.

        """

        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            echo = kwargs.pop("echo", False)
            result = f(*args, **kwargs)

            if echo is True:
                sys.stdout.write(result.output)

            # if result.exception is not None:
            # raise result.exception

            return result

        return wrapper

    class_.invoke = invoke_wrapper(class_.invoke)
    cli_runner = class_()

    yield cli_runner
