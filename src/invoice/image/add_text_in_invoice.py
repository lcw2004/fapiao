# -*- coding: utf-8 -*-
import logging
from PIL import Image, ImageDraw

from invoice.bean.beans import Invoice
from invoice.common import config
from invoice.common import money_convert
from invoice.image import image_util


logger = logging.getLogger(__name__)

def add_text_in_image(out_img_path, invoice_id, in_img_path=config.PATH_OF_INVOICE_TEMPLATE_BLANK):
    invoice = Invoice.get(id=invoice_id)
    invoice_detail_list = list(Invoice.get(id=invoice_id).invoiceDetails)
    add_text_in_image_by_invoice(out_img_path, invoice, invoice_detail_list, in_img_path)

def add_text_in_image_by_invoice(out_img_path, invoice, invoice_detail_list, in_img_path=config.PATH_OF_INVOICE_TEMPLATE_BLANK):
    logging.info(u"图片模板:" + in_img_path)

    # 打开图片
    im = Image.open(in_img_path)

    # 画文本
    draw = ImageDraw.Draw(im)
    image_util.add_text_in_image(draw, "custom_name", invoice.custom.name)
    image_util.add_text_in_image(draw, "start_time", invoice.start_time)
    # image_util.add_text_in_image(draw, "invoice_num", invoice.invoice_num)
    image_util.add_text_in_image(draw, "drawer", invoice.drawer)
    image_util.add_text_in_image(draw, "beneficiary", invoice.beneficiary)
    image_util.add_text_in_image(draw, "reviewer", invoice.reviewer)
    image_util.add_text_in_image(draw, "total_num", invoice.total_num)
    total_num_cn = money_convert.to_rmb_upper(invoice.total_num)
    image_util.add_text_in_image(draw, "total_num_cn", total_num_cn)

    up_offset = 0
    for invoice_detail in invoice_detail_list:
        image_util.add_text_in_image(draw, "code", invoice_detail.product.code, up_offset)
        image_util.add_text_in_image(draw, "name", invoice_detail.product.name, up_offset)
        image_util.add_text_in_image(draw, "pro_num", invoice_detail.pro_num, up_offset)
        image_util.add_text_in_image(draw, "unit_price", invoice_detail.product.unit_price, up_offset)
        image_util.add_text_in_image(draw, "contain_tax_price", invoice_detail.contain_tax_price, up_offset)
        up_offset += 60

    if invoice.status == -1:
        image_util.add_text_in_image(draw, "zuofei", u"作 废")
        # im_zuofei = Image.open(config.PATH_OF_ZUOFEI_IMG)
        # im_width, im_height = im.size
        # im_zuofei_width, im_zuofei_height = im_zuofei.size
        # zuofei_pos_x = (im_width - im_zuofei_width) / 2
        # zuofei_pos_y = (im_height - im_zuofei_height) / 2
        # im = image_util.add_watermark(im, im_zuofei, zuofei_pos_x, zuofei_pos_y, opacity=0.7)

    # 显示
    # im.show()
    im.save(out_img_path)


if __name__ == "__main__":
    img_path = "D:\\Invoice_template_1.png"
    out_img_path = "D:\\12_text.jpg"
    mark_img_path = "D:\\zuofei.png"
    add_text_in_image(out_img_path, 1, img_path)
