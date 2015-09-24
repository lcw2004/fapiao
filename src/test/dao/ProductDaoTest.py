# -*- coding: UTF-8 -*-

from invoice.bean.ProductBean import Product
from invoice.dao.ProductDao import ProductDao


def testSave():
    product = Product()
    product.name = "name"
    product.code = "code"
    product.type = "type"
    product.unit_price = "unit_price"
    product.tax_price = "tax_price"
    product.tax = "tax"
    product.business_tax_num = "business_tax_num"
    product.erp_id = "erp_id"
    product.col1 = "col1"
    product.col2 = "col2"
    product.col3 = "col3"
    product.col4 = "col4"

    productDao = ProductDao()
    productDao.save(product)

def testGet():
    productDao = ProductDao()
    list = productDao.get()
    for product in list:
        print "------------------------"
        print product.id
        print product.name
        print product.code
        print product.type
        print product.unit_price
        print product.tax_price
        print product.tax
        print product.business_tax_num
        print product.erp_id
        print product.col1
        print product.col2
        print product.col3
        print product.col4


if __name__ == "__main__":
    testSave()
    testGet()
