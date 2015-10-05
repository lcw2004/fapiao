# -*- coding: UTF-8 -*-

import sqlite3

zidian_db_path = "data.db"

class BaseDao:
    def __init__(self):
        self.connect = sqlite3.connect(zidian_db_path)