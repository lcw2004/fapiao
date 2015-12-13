# -*- coding: UTF-8 -*-
from invoice.common import config
from invoice.common.settings import Settings


class TextInfo:
    def __init__(self, font_name, font_size, font_color, x_pos, y_pos):
        self.font_name = font_name
        self.font_size = font_size
        self.font_color = font_color
        self.x_pos = x_pos
        self.y_pos = y_pos


class TextInfoFactory:
    def __init__(self):
        default_font_name = Settings.value_str(Settings.TEMP_FONT_NAME)
        default_font_size = Settings.value_int(Settings.TEMP_FONT_SIZE)
        default_font_color = config.DEFAULT_FONT_COLOR

        self.text_info_map = {}
        self.text_info_map["default"] = TextInfo(default_font_name, default_font_size, default_font_color, 100, 20)
        # 客户名称
        self.text_info_map["custom_name"] = TextInfo(default_font_name, default_font_size, default_font_color, 387, 303)
        # 开票日期
        self.text_info_map["start_time"] = TextInfo(default_font_name, default_font_size, default_font_color, 1155, 303)
        # 发票号码
        self.text_info_map["invoice_num"] = TextInfo(default_font_name, default_font_size, default_font_color, 1690, 250)
        # 开票人
        self.text_info_map["drawer"] = TextInfo(default_font_name, default_font_size, default_font_color, 355, 929)
        # 收款人
        self.text_info_map["beneficiary"] = TextInfo(default_font_name, default_font_size, default_font_color, 769, 929)
        # 复核人
        self.text_info_map["reviewer"] = TextInfo(default_font_name, default_font_size, default_font_color, 1185, 929)
        # 总金额
        self.text_info_map["total_num_cn"] = TextInfo(default_font_name, default_font_size, default_font_color, 501, 829)
        self.text_info_map["total_num"] = TextInfo(default_font_name, default_font_size, default_font_color, 1724, 826)
        # 产品代码
        self.text_info_map["code"] = TextInfo(default_font_name, default_font_size, default_font_color, 193, 500)
        # 产品名称
        self.text_info_map["name"] = TextInfo(default_font_name, default_font_size, default_font_color, 487, 500)
        self.text_info_map["pro_num"] = TextInfo(default_font_name, default_font_size, default_font_color, 1080, 500)
        self.text_info_map["unit_price"] = TextInfo(default_font_name, default_font_size, default_font_color, 1323, 500)
        self.text_info_map["contain_tax_price"] = TextInfo(default_font_name, default_font_size, default_font_color, 1640, 500)


if __name__ == "__main__":
    factory = TextInfoFactory()
    for key in factory.text_info_map:
        text_info = factory.text_info_map[key]
        print key + " : " + text_info.font_name, text_info.font_size, text_info.font_color, text_info.x_pos, text_info.y_pos
