# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont

font_path = "C:\\Windows\\Fonts\\simfang.ttf"
font_size = 40
font_color = (0,0,0,0)
img_path = "D:\\12.jpg"
out_img_path = "D:\\12_text.jpg"

# 打开图片
im = Image.open(img_path)

# 画文本
draw = ImageDraw.Draw(im)
fnt = ImageFont.truetype(font_path, font_size)
draw.text((100,100), u"我Hello", font=fnt, fill=font_color)
draw.text((100,160), "World", font=fnt, fill=font_color)
draw.text((100,260), "World", font=fnt, fill=font_color)

im.save(out_img_path)
# 显示
im.show()