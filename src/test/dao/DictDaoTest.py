# -*- coding: UTF-8 -*-
from invoice.dao.DictDao import DictDao

if __name__ == "__main__":
    dictDao = DictDao()
    print dictDao.get(type="EXCEL_TO_XML")