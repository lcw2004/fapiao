# -*- coding: UTF-8 -*-
import xlsxwriter

from invoice.bean.beans import Invoice

class InvoiceElsxExporter:
    def __init__(self, file_name):
        self.workbook = xlsxwriter.Workbook(file_name)
        self.datetime_format = self.workbook.add_format({'num_format': 'yyyy-mm-dd hh:mm:ss'})
        self.money = self.workbook.add_format({'num_format': u'#,###元'})
        # 头部标题格式
        header_format = self.workbook.add_format()
        header_format.set_bold()
        header_format.set_font_size(15)

    def add_invoice_sheet(self, sheet_name, invoice_list):
        worksheet = self.workbook.add_worksheet(sheet_name)
        self.add_headers(worksheet)

        # 将发票信息填到Excel中
        row_count = len(invoice_list)
        for i in range(row_count):
            row_num = i + 1
            invoice = invoice_list[i]
            worksheet.write(row_num, 0, invoice.invoice_num)
            worksheet.write(row_num, 1, invoice.custom.name)
            worksheet.write_datetime(row_num, 2, invoice.start_time, self.datetime_format)
            worksheet.write(row_num, 3, invoice.total_num, self.money)
            worksheet.write(row_num, 4, invoice.drawer)
            worksheet.write(row_num, 5, invoice.beneficiary)
            worksheet.write(row_num, 6, invoice.reviewer)

    def close(self):
        self.workbook.close()

    def add_headers(self, worksheet):
        # 标题文本
        headers = [u"发票号码", u"客户名称", u"开票日期", u"金额", u"开票人", u"收款人", u"复核人"]

        # 添加标题到Excel中
        header_count = len(headers)
        for i in range(header_count):
            worksheet.set_column(0, i, 20)
            worksheet.write(0, i, headers[i], self.header_format)

if __name__ == "__main__":
    file_name = u'发票列表.xlsx'
    invoice_list = list(Invoice.select().where(Invoice.status == 1))
    zuofei_invoice_list = list(Invoice.select().where(Invoice.status == 0))

    elxs_exporter = InvoiceElsxExporter(file_name)
    elxs_exporter.add_invoice_sheet(u"已开发票", invoice_list)
    elxs_exporter.add_invoice_sheet(u"作废发票", zuofei_invoice_list)
    elxs_exporter.close()


