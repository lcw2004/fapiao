__author__ = 'Administrator'

class Product:
    def __init__(self):
        # ID
        self.id = None
        # 产品名称
        self.name = None
        # 产品代码
        self.code = None
        # 产品型号
        self.type = None
        # 产品单价
        self.unit_price = None
        # 含税单价
        self.tax_price = None
        # 税率
        self.tax = None
        # 企业税号
        self.business_tax_num = None
        # ERA对照值
        self.erp_id = None
        self.col1 = None
        self.col2 = None
        self.col4 = None

        # 父ID
        self.p_id = None