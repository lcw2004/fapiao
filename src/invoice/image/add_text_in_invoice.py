# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw

from invoice.bean.beans import Invoice
from invoice.common import config
from invoice.image import image_util


def add_text_in_image(in_img_path, out_img_path):
    invoice_id = 1
    invoice = Invoice.get(id=invoice_id)
    invoice_detail_list = list(Invoice.get(id=invoice_id).invoiceDetails)

    # 打开图片
    im = Image.open(in_img_path)

    # 画文本
    draw = ImageDraw.Draw(im)
    image_util.add_text(draw, "custom_name", invoice.custom.name)
    image_util.add_text(draw, "start_time", invoice.start_time)
    image_util.add_text(draw, "invoice_num", invoice.invoice_num)
    image_util.add_text(draw, "drawer", invoice.drawer)
    image_util.add_text(draw, "beneficiary", invoice.beneficiary)
    image_util.add_text(draw, "reviewer", invoice.reviewer)
    # add_text(draw, "total_num_cn", invoice.total_num)
    # add_text(draw, "total_num", invoice.total_num)

    for invoice_detail in invoice_detail_list:
        image_util.add_text(draw, "code", invoice_detail.product.code)
        image_util.add_text(draw, "name", invoice_detail.product.name)
        image_util.add_text(draw, "pro_num", invoice_detail.pro_num)
        image_util.add_text(draw, "unit_price", invoice_detail.product.unit_price)
        image_util.add_text(draw, "contain_tax_price", invoice_detail.contain_tax_price)

    im_zuofei = Image.open(config.PATH_OF_ZUOFEI_IMG)
    im_width, im_height = im.size
    im_zuofei_width, im_zuofei_height = im_zuofei.size
    im = image_util.add_watermark(im, im_zuofei, (im_width-im_zuofei_width) / 2, (im_height-im_zuofei_height) / 2, opacity=0.7)

    # 显示
    im.show()
    im.save(out_img_path)

if __name__ == "__main__":
    img_path = "D:\\Invoice_template.png"
    out_img_path = "D:\\12_text.jpg"
    add_text_in_image(img_path, out_img_path)



