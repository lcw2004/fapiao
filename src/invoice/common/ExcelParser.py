__author__ = 'Administrator'
# -*- coding: UTF-8 -*-

import xlrd

data = xlrd.open_workbook('Test.xls')

table = data.sheets()[0]

nrows = table.nrows
ncols = table.ncols

for i in range(nrows):
    row = table.row_values(i)

    col = row[0]

    print row

