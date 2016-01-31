# -*- coding: utf-8 -*-
from invoice.bean.beans import *


def save_or_update_custom(custom_name):
    try:
        custom_of_this = Custom.get(name=custom_name)
    except Exception:
        custom_of_this = Custom.create(name=custom_name)
        custom_of_this.save()
    return custom_of_this


def save_or_update_product(product_name, product_code, product_unit_price):
    try:
        product_of_this = Product.get(Product.name == product_name)
    except Exception:
        product_of_this = Product.create(name=product_name,
                                         code=product_code,
                                         unit_price=product_unit_price
                                         )
        product_of_this.save()
    return product_of_this


def save_or_update_invoice(invoice):
    if invoice.id:
        q = Invoice.update(invoice_num=invoice.invoice_num,
                           invoice_code=invoice.invoice_code,
                           total_num=invoice.total_num,
                           drawer=invoice.drawer,
                           beneficiary=invoice.beneficiary,
                           reviewer=invoice.reviewer,
                           custom=invoice.custom).where(Invoice.id == invoice.id)
        q.execute()
    else:
        invoice = Invoice.create(invoice_num=invoice.invoice_num,
                                 invoice_code=invoice.invoice_code,
                                 total_num=invoice.total_num,
                                 drawer=invoice.drawer,
                                 beneficiary=invoice.beneficiary,
                                 reviewer=invoice.reviewer,
                                 custom=invoice.custom)
        invoice.save()
    return invoice


def save_or_update_invoice_detail(invoice_detail):
    if invoice_detail.id:
        q = InvoiceDetail.update(pro_num=invoice_detail.pro_num,
                                 contain_tax_price=invoice_detail.contain_tax_price,
                                 not_tax_price=invoice_detail.not_tax_price,
                                 product=invoice_detail.product,
                                 invoice=invoice_detail.invoice).where(InvoiceDetail.id == invoice_detail.id)
        q.execute()
    else:
        invoice_detail = InvoiceDetail.create(
            pro_num=invoice_detail.pro_num,
            contain_tax_price=invoice_detail.contain_tax_price,
            not_tax_price=invoice_detail.not_tax_price,
            product=invoice_detail.product,
            invoice=invoice_detail.invoice
        )
        invoice_detail.save()
    return invoice_detail
