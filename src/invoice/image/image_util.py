# -*- coding: utf-8 -*-

import ImageEnhance
from PIL import Image, ImageDraw, ImageFont
from invoice.common import common_util
from invoice.image.text_position import TextInfoFactory

def add_text_in_image(draw, text_name, text_value):
    """
    往图片中添加文本
    :param draw:画笔
    :param text_name:文本名称，用于取文本字体大小及坐标
    :param text_value:文本值
    :return:
    """
    text_info = TextInfoFactory().text_info_map[text_name]
    font_name = text_info.font_name
    font_size = text_info.font_size
    font_color = text_info.font_color
    x_pos = text_info.x_pos
    y_pos = text_info.y_pos
    fnt = ImageFont.truetype(font_name, font_size)

    text_value_str = common_util.to_string_trim(text_value)

    draw.text((x_pos, y_pos), text_value_str, font=fnt, fill=font_color)

def reduce_opacity(im, opacity):
    """
    返回一个指定的透明度的图片
    :param im: 图片
    :param opacity: 图片透明度，1 - 不透明
    :return:
    """
    assert opacity >= 0 and opacity <= 1
    if im.mode != 'RGBA':
        im = im.convert('RGBA')
    else:
        im = im.copy()
    alpha = im.split()[3]

    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    im.putalpha(alpha)
    return im

def add_watermark(base_image, mark_image, x_pos, y_pox, opacity=1):
    """
    往图片上添加水印图片
    :param imagefile: 图片文件路径
    :param markfile:水印文件路径
    :param opacity:透明度
    :param x_pos:X坐标
    :param y_pox:Y坐标
    :return:
    """
    if opacity < 1:
        mark_image = reduce_opacity(mark_image, opacity)
    if base_image.mode != 'RGBA':
        base_image = base_image.convert('RGBA')

    new_image = Image.new('RGBA', base_image.size, (0, 0, 0, 0))
    new_image.paste(mark_image,(x_pos, y_pox))

    return Image.composite(new_image, base_image, new_image)

if __name__ == "__main__":
    img_path = "D:\\Invoice_template.png"
    out_img_path = "D:\\12_text.jpg"
    mark_img_path = "D:\\zuofei.png"
    add_watermark(Image.open(img_path), Image.open(mark_img_path), 100, 100, opacity=0.5).show()