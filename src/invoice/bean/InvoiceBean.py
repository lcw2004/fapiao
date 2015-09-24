# -*- coding: UTF-8 -*-

class Invoice:
    def __init__(self):
        self.id = None
        self.invoice_num = None
        self.custom_id = None
        self.remark = None
        self.start_time = None
        self.total_not_tax = None
        self.total_tax = None
        self.total_num = None
        self.serial_number = None
        self.drawer = None
        self.beneficiary = None
        self.reviewer = None
        self.status = 0

        # 客户对象
        self.custom = None

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
