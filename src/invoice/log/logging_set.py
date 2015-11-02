# -*- coding: utf-8 -*-

import os
import json
import logging.config


def setup_logging(default_path='logging.json', default_level=logging.INFO, env_key='LOG_CFG'):
    """
    加载日志配置文件
    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)

        logger = logging.getLogger(__name__)
        logger.info(u"成功加载日志配置:{0}".format(default_path))
    else:
        logging.basicConfig(level=default_level)