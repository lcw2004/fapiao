__author__ = 'Administrator'

BASE_PATH = ""
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