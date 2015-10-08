# -*- coding: UTF-8 -*-

class InvoiceDetail:
    def __init__(self):
        # ID
        self.id = None
        # 产品代码
        self.pro_code = None
        # 产品名称
        self.pro_name = None
        # 产品型号
        self.pro_type = None
        # 产品单位
        self.pro_unit = None
        # 产品单价
        self.pro_unit_price = 0
        # 产品数量
        self.pro_num = 0
        # 含税单价
        self.tax_price = 0
        # 税率
        self.tax_rate = 0.17
        # 税额
        self.tax = None
        # 发票ID
        self.invoice_Id = None

        # invoice对象
        self.invoice = None
