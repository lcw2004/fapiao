# -*- coding: UTF-8 -*-

class Invoice:
    def __init__(self):
        # ID
        self.id = None
        # 发票号码
        self.invoice_num = None
        # 客户ID
        self.custom_id = None
        # 备注
        self.remark = None
        # 开票日期
        self.start_time = None
        # 总不含税金额
        self.total_not_tax = None
        # 总税额
        self.total_tax = None
        # 价税合计
        self.total_num = None
        # 系统流水号
        self.serial_number = None
        # 开票人
        self.drawer = None
        # 收款人
        self.beneficiary = None
        # 复核人
        self.reviewer = None
        # 发票产生标志， 0 - 未开票， 1 - 已开票， -1 - 已删除
        self.status = 0

        # 客户对象
        self.custom = None

        # 详细信息列表
        self.invoiceDetailList = None

    def toString(self):
        print "invoice_num : ", self.invoice_num, \
            ", custom_id: ", self.custom_id, \
            ", start_time: ", self.start_time, \
            ", total_not_tax: ", self.total_not_tax, \
            ", total_tax: ", self.total_tax, \
            ", total_num: ", self.total_num, \
            ", serial_number: ", self.serial_number, \
            ", drawer: ", self.drawer, \
            ", beneficiary: ", self.beneficiary, \
            ", reviewer: ", self.reviewer, \
            ", status: ", self.status, \
            ", remark: ", self.remark