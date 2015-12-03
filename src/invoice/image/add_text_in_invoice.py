# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
from invoice.bean.beans import Invoice
from invoice.image.text_position import *


def add_text(draw, text_name, text_value):
    text_info = TextInfoFactory().text_info_map[text_name]
    font_name = text_info.font_name
    font_size = text_info.font_size
    font_color = text_info.font_color
    x_pos = text_info.x_pos
    y_pos = text_info.y_pos
    fnt = ImageFont.truetype(font_name, font_size)
    draw.text((x_pos, y_pos), text_value, font=fnt, fill=font_color)

def add_text_in_image(in_img_path, out_img_path):
    invoice = Invoice.get(id=1)

    # 打开图片
    im = Image.open(in_img_path)

    # 画文本
    draw = ImageDraw.Draw(im)

    add_text(draw, "custom_name", invoice.custom.name)
    # add_text(draw, "start_time", invoice.start_time)
    add_text(draw, "invoice_num", invoice.invoice_num)
    # add_text(draw, "drawer", invoice.drawer)
    # add_text(draw, "beneficiary", invoice.beneficiary)
    # add_text(draw, "reviewer", invoice.reviewer)
    # add_text(draw, "total_num_cn", invoice.total_num)
    # add_text(draw, "total_num", invoice.total_num)
    # add_text(draw, "code", invoice)
    # add_text(draw, "name", invoice.custom)
    # add_text(draw, "pro_num", invoice.custom)
    # add_text(draw, "unit_price", invoice.custom)
    # add_text(draw, "contain_tax_price", invoice.custom)

    # 显示
    im.show()

if __name__ == "__main__":
    img_path = "D:\\12.jpg"
    out_img_path = "D:\\12_text.jpg"
    add_text_in_image(img_path, out_img_path)



