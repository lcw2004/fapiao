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
        self.text_info_map["default"] = TextInfo(default_font_name, default_font_size, default_font_color, 100, 100)
        # 客户名称
        self.text_info_map["custom_name"] = TextInfo(default_font_name, default_font_size, default_font_color, 397, 343)
        # 开票日期
        self.text_info_map["start_time"] = TextInfo(default_font_name, default_font_size, default_font_color, 1145, 343)
        # 发票号码
        self.text_info_map["invoice_num"] = TextInfo(default_font_name, default_font_size, default_font_color, 1690, 280)
        # 开票人
        self.text_info_map["drawer"] = TextInfo(default_font_name, default_font_size, default_font_color, 355, 1029)
        # 收款人
        self.text_info_map["beneficiary"] = TextInfo(default_font_name, default_font_size, default_font_color, 769, 1029)
        # 复核人
        self.text_info_map["reviewer"] = TextInfo(default_font_name, default_font_size, default_font_color, 1185, 1029)
        # 总金额
        self.text_info_map["total_num_cn"] = TextInfo(default_font_name, default_font_size, default_font_color, 501, 919)
        self.text_info_map["total_num"] = TextInfo(default_font_name, default_font_size, default_font_color, 1724, 916)
        # 产品代码
        self.text_info_map["code"] = TextInfo(default_font_name, default_font_size, default_font_color, 193, 580)
        # 产品名称
        self.text_info_map["name"] = TextInfo(default_font_name, default_font_size, default_font_color, 487, 580)
        self.text_info_map["pro_num"] = TextInfo(default_font_name, default_font_size, default_font_color, 1080, 580)
        self.text_info_map["unit_price"] = TextInfo(default_font_name, default_font_size, default_font_color, 1323, 580)
        self.text_info_map["contain_tax_price"] = TextInfo(default_font_name, default_font_size, default_font_color, 1640, 580)


if __name__ == "__main__":
    factory = TextInfoFactory()
    for key in factory.text_info_map:
        text_info = factory.text_info_map[key]
        print key + " : " + text_info.font_name, text_info.font_size, text_info.font_color, text_info.x_pos, text_info.y_pos
