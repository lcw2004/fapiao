# -*- coding: UTF-8 -*-

########## 程序基础配置 ##########
# 日志配置文件路径
PATH_OF_LOGGING = "resources/logging.json"
# 数据库路径
# PATH_OF_DATABASE = "resources/data.db"
PATH_OF_DATABASE = r"E:\个人文档（需要整理）\OpenSource\fapiao\src\resources\data.db"
########## 程序基础配置 ##########

########## 模板配置 ##########
# 模板图片路径
PATH_OF_INVOICE_TEMPLATE = "resources/Invoice_template.png"
# 作废章路径
PATH_OF_ZUOFEI_IMG = "resources/zuofei.png"
########## 模板配置 ##########

########## 航空金税接口配置 ##########
PATH_OF_XML = "resources/input.xml"
INPUT_PATH = "D:\\invoince\\input\\"
OUTPUT_PATH = "D:\\invoince\\output\\"
TEMP_PATH = "D:\\invoince\\temp\\"
########## 航空金税接口配置 ##########


def getConfigInDB(label):
    from invoice.bean.beans import Dict
    dict = Dict.get(Dict.label == label)
    return dict

if __name__ == "__main__":
    print getConfigInDB("EXCEL_START_ROW_NUM").value