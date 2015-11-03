# -*- coding: UTF-8 -*-

import datetime
from peewee import *
from invoice.common import config


db = SqliteDatabase(config.DATABASE_PATH)

class BaseModel(Model):
    """
    基础类
    """

    # ID
    id = PrimaryKeyField()

    class Meta:
        database = db


class Custom(BaseModel):
    """
    客户表
    """

    # 客户代码
    code = TextField(null=True)
    # 客户名称
    name = TextField()
    # 客户税号
    tax_id = TextField(null=True)
    # 开户银行账号
    bank_account = TextField(null=True)
    # 客户地址
    addr = TextField(null=True)
    # 企业税号
    business_tax_di = TextField(null=True)
    # ERP对照值
    erp_id = TextField(null=True)
    # 开票汇总名称
    summary_title = TextField(null=True)
    # 备注
    remark=TextField(null=True)

    class Meta:
        db_table = 'tbl_custom'


class Product(BaseModel):
    """
    产品表
    """

    # 产品代码
    code = TextField(null=True)
    # 产品名称
    name = TextField(null=True)
    # 产品型号
    type = TextField(null=True)
    # 产品单位
    unit = TextField(null=True)
    # 产品单价
    unit_price = FloatField(default=0)
    # 含税单价（产品单价 + 产品单价 * 税率）
    tax_price = FloatField(default=0)
    # 税率
    tax = FloatField(default=0.17)
    # 企业税号
    business_tax_num = TextField(null=True)
    # ERA对照值
    erp_id = TextField(null=True)
    col1 = TextField(null=True)
    col2 = TextField(null=True)
    col3 = TextField(null=True)
    col4 = TextField(null=True)
    # 父ID
    p_id = IntegerField(default=0.17)

    class Meta:
        db_table = 'tbl_product'


class Dict(BaseModel):
    """
    字典表
    """

    label = TextField(null=True)
    value = TextField(null=True)
    type = TextField(null=True)
    describe = TextField(null=True)
    status = IntegerField(null=True)
    oindex = IntegerField(null=True)

    class Meta:
        db_table = 'tbl_dict'


class Invoice(BaseModel):
    """
    发票表
    """

    # 发票号码
    invoice_num = TextField()
    # 备注
    remark = TextField(null=True)
    # 开票日期
    start_time = DateTimeField(default=datetime.datetime.now)
    # 总不含税金额（即Excel中录入的金额）
    total_not_tax = FloatField(default=0)
    # 总税额（即不含税金额 * 税率）
    total_tax = FloatField(default=0)
    # 价税合计（总不含税金额 + 总税额）
    total_num = FloatField(default=0)
    # 系统流水号
    serial_number = TextField(null=True)
    # 开票人
    drawer = TextField(null=True)
    # 收款人
    beneficiary = TextField(null=True)
    # 复核人
    reviewer = TextField(null=True)
    # 发票产生标志， 0 - 未开票， 1 - 已开票， -1 - 已删除
    status = IntegerField(default=0)
    # 客户对象
    custom = ForeignKeyField(Custom, db_column='custom_id')

    class Meta:
        db_table = 'tbl_invoice'


class InvoiceDetail(BaseModel):
    """
    发票详细信息表
    """

    # 产品数量
    pro_num = IntegerField(default=0)
    # 不含税金额（Excel中的金额）
    not_tax_price = FloatField(default=0)
    # 税额（不含税金额 * 税率）
    tax_price = FloatField(default=0)
    # 含税金额（不含税金额 + 税额）
    contain_tax_price = FloatField(default=0)
    # invoice对象
    invoice = ForeignKeyField(Invoice, db_column='invoice_Id', related_name='invoiceDetails')
    # 产品对象
    product = ForeignKeyField(Product, db_column='product_id')

    class Meta:
        db_table = 'tbl_invoice_detail'

