# -*- coding: UTF-8 -*-

# ============ 程序基础配置 ============
# 日志配置文件路径
PATH_OF_LOGGING = "resources/logging.json"
# 数据库路径
# PATH_OF_DATABASE = "resources/data.db"
PATH_OF_DATABASE = r"E:\个人文档（需要整理）\OpenSource\fapiao\src\resources\data.db"
# ============ 程序基础配置 ============

# ============ 模板配置 ============
# 模板图片路径
PATH_OF_INVOICE_TEMPLATE = "resources/Invoice_template.png"
# 作废章路径
PATH_OF_ZUOFEI_IMG = "resources/zuofei.png"
DEFAULT_FONT_NAME = "C:\\Windows\\Fonts\\simfang.ttf"
DEFAULT_FONT_SIZE = 38
DEFAULT_FONT_COLOR = (0, 0, 0, 0)
# ============ 模板配置 ============

# ============ 航空金税接口配置 ============
PATH_OF_XML = "resources/input.xml"
INPUT_PATH = "D:\\invoince\\input\\"
OUTPUT_PATH = "D:\\invoince\\output\\"
TEMP_PATH = "D:\\invoince\\temp\\"
# ============ 航空金税接口配置 ============


def get_config_from_database(label):
    from invoice.bean.beans import Dict
    return Dict.get(Dict.label == label)


if __name__ == "__main__":
    print get_config_from_database("EXCEL_START_ROW_NUM").value
