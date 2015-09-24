__author__ = 'Administrator'

# BASE_PATH = "E:\\OpenSource\\GitHub\\fapiao\src\\"
BASE_PATH = "D:\\GitHub\\fapiao\\src\\"
DATABASE_PATH = BASE_PATH + "data.db"

def getConfigInDB(label, type=None):
    from invoice.dao.DictDao import DictDao
    dictDao = DictDao()
    dict = dictDao.one(type, label)
    return dict

if __name__ == "__main__":
    print getConfigInDB("EXCEL_START_ROW_NUM").value