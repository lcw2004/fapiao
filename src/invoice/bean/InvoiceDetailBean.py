# -*- coding: UTF-8 -*-

class InvoiceDetail:
    def __init__(self):
        # ID
        self.id = None

        # 产品数量
        self.pro_num = 0
        # 不含税金额（Excel中的金额）
        self.not_tax_price = 0
        # 税额（不含税金额 * 税率）
        self.tax_price = 0
        # 含税金额（不含税金额 + 税额）
        self.contain_tax_price = 0

        # 发票ID
        self.invoice_Id = None
        # 产品ID
        self.product_id = None

        # invoice对象
        self.invoice = None
        # 产品对象
        self.product = None

    def caculate(self):
        self.tax_price = float(self.not_tax_price) * float(self.product.tax)
        self.contain_tax_price = float(self.not_tax_price) + self.tax_price