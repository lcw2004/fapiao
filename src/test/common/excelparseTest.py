__author__ = 'Administrator'

from invoice.common.excelparse import parse_excel_to_invoice_list

if __name__ == "__main__":
    invoiceDetailList = parse_excel_to_invoice_list("C:\\Users\\Administrator\\Desktop\\data.xls")
    for i in range(len(invoiceDetailList)):
        invoiceDetail = invoiceDetailList[i]
        print "--------------------------------------"
        print invoiceDetail.invoice.custom.name
        print invoiceDetail.invoice.invoice_num
        print invoiceDetail.invoice.total_not_tax
        print invoiceDetail.invoice.remark
        print invoiceDetail.pro_type
        print invoiceDetail.pro_name
        print "--------------------------------------"