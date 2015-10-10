__author__ = 'Administrator'


import os

print os.getcwd()
print os.path.abspath(os.curdir)
print os.path.abspath('.')
# BASE_PATH = "E:\\OpenSource\\GitHub\\fapiao\src\\"
BASE_PATH = "D:\\GitHub\\fapiao\\src\\"
DATABASE_PATH = BASE_PATH + "data.db"
INPUT_PATH = "D:\\invoince\\Input\\"
OUTPUT_PATH = "D:\\invoince\\Output\\"
TEMP_PATH = "D:\\invoince\\TEMP\\"
XML_PATH = BASE_PATH + "input.xml"

def getConfigInDB(label, type=None):
    from invoice.dao.DictDao import DictDao
    dictDao = DictDao()
    dict = dictDao.one(type, label)
    return dict

if __name__ == "__main__":
    print getConfigInDB("EXCEL_START_ROW_NUM").value