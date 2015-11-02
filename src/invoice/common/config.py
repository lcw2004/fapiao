# -*- coding: UTF-8 -*-

DATABASE_PATH = "data.db"
XML_PATH = "input.xml"

INPUT_PATH = "D:\\invoince\\Input\\"
OUTPUT_PATH = "D:\\invoince\\Output\\"
TEMP_PATH = "D:\\invoince\\TEMP\\"

def getConfigInDB(label):
    from invoice.bean.beans import Dict
    dict = Dict.get(Dict.label == label)
    return dict

if __name__ == "__main__":
    print getConfigInDB("EXCEL_START_ROW_NUM").value