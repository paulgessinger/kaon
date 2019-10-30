import os
import socket
from typing import Any, Dict, Optional

import click
import yaml
import schema as sc


APP_NAME = "kaon"
APP_DIR = click.get_app_dir(APP_NAME, force_posix=True)
CONFIG_FILE = os.path.join(APP_DIR, "config.yml")
DB_FILE = os.path.join(APP_DIR, "database.sqlite")

config_schema = sc.Schema({})

class Config:
    def __init__(
        self, data: Optional[Dict[str, Any]] = None
    ) -> None:
        if data is not None:
            self.data = data
        else:
            with open(CONFIG_FILE) as f:
                self.data = yaml.safe_load(f)

        self.data = config_schema.validate(self.data)

    def __getattr__(self, key: str) -> Any:
        return self.data[key]
