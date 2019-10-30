import os
from typing import Optional, Any, Dict

import click
import yaml

from . import config
from .logger import logger


def setup(cfg: Optional[config.Config]) -> None:
    logger.debug("Running setup")
    if not os.path.exists(config.APP_DIR):
        os.makedirs(config.APP_DIR)

    data: Dict[str, Any]
    if cfg is None:
        data = config.config_schema.validate({})
    else:
        data = dict(cfg.data)

    logger.debug("Config: %s", data)
    with open(config.CONFIG_FILE, "w") as f:
        yaml.dump(data, f)
