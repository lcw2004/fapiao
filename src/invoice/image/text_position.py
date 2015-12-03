# -*- coding: UTF-8 -*-

class TextInfo:
    def __init__(self, font_name, font_size, font_color, x_pos, y_pos):
        self.font_name = font_name
        self.font_size = font_size
        self.font_color = font_color
        self.x_pos = x_pos
        self.y_pos = y_pos

class TextInfoFactory:
    def __init__(self):
        default_font_name = "C:\\Windows\\Fonts\\simfang.ttf"
        default_font_size = 35
        default_font_color = (0,0,0,0)

        self.text_info_map = {}
        self.text_info_map["default"] = TextInfo(default_font_name, default_font_size, default_font_color, 100, 100)
        # 客户名称
        self.text_info_map["custom_name"] = TextInfo(default_font_name, default_font_size, default_font_color, 324, 280)
        # 开票日期
        self.text_info_map["start_time"] = TextInfo(default_font_name, default_font_size, default_font_color, 864, 280)
        # 发票号码
        self.text_info_map["invoice_num"] = TextInfo(default_font_name, default_font_size, default_font_color, 1239, 239)
        # 开票人
        self.text_info_map["drawer"] = TextInfo(default_font_name, default_font_size, default_font_color, 278, 750)
        # 收款人
        self.text_info_map["beneficiary"] = TextInfo(default_font_name, default_font_size, default_font_color, 579, 750)
        # 复核人
        self.text_info_map["reviewer"] = TextInfo(default_font_name, default_font_size, default_font_color, 863, 750)
        # 总金额
        self.text_info_map["total_num_cn"] = TextInfo(default_font_name, default_font_size, default_font_color, 423, 676)
        self.text_info_map["total_num"] = TextInfo(default_font_name, default_font_size, default_font_color, 1299, 676)
        # 产品代码
        self.text_info_map["code"] = TextInfo(default_font_name, default_font_size, default_font_color, 189, 438)
        # 产品名称
        self.text_info_map["name"] = TextInfo(default_font_name, default_font_size, default_font_color, 420, 438)
        self.text_info_map["pro_num"] = TextInfo(default_font_name, default_font_size, default_font_color, 812, 438)
        self.text_info_map["unit_price"] = TextInfo(default_font_name, default_font_size, default_font_color, 989, 438)
        self.text_info_map["contain_tax_price"] = TextInfo(default_font_name, default_font_size, default_font_color, 1218, 438)


if __name__ == "__main__":
    factory = TextInfoFactory()
    for key in factory.text_info_map:
        text_info = factory.text_info_map[key]
        print key + " : " + text_info.font_name, text_info.font_size, text_info.font_color, text_info.x_pos, text_info.y_pos
