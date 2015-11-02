__author__ = 'Administrator'



BASE_PATH = "D:\\GitHub\\fapiao\\src\\"
DATABASE_PATH = BASE_PATH + "data.db"
INPUT_PATH = "D:\\invoince\\Input\\"
OUTPUT_PATH = "D:\\invoince\\Output\\"
TEMP_PATH = "D:\\invoince\\TEMP\\"
XML_PATH = BASE_PATH + "input.xml"

def getConfigInDB(label):
    from invoice.bean.beans import Dict
    dict = Dict.get(Dict.label == label)
    return dict

if __name__ == "__main__":
    print getConfigInDB("EXCEL_START_ROW_NUM").value