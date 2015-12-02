# -*- coding: utf-8 -*-
from PyQt4 import QtGui

from PyQt4.QtCore import QRect, QPoint, QSize, Qt
from PyQt4.QtGui import QPrinter, QPrintPreviewDialog, QPainter, QPixmap, QApplication, QTableWidget, QTableWidgetItem, \
    QPushButton, QWidget, QVBoxLayout

__author__ = 'Administrator'


def on_picButton_clicked():
    printer = QPrinter(QPrinter.HighResolution)
    # /* 打印预览 */
    preview = QPrintPreviewDialog(printer, widget)

    """
     * QPrintPreviewDialog类提供了一个打印预览对话框，里面功能比较全，
     * paintRequested(QPrinter *printer)是系统提供的，
     * 当preview.exec()执行时该信号被触发，
     * plotPic(QPrinter *printer)是用户自定义的槽函数，图像的绘制就在这个函数里。
    """
    preview.paintRequested.connect(plotPic)
    preview.exec_()


def plotPic(printer):
    painter = QPainter(printer)
    image = QtGui.QPixmap("D:\\1.jpg")


    rect = painter.viewport()
    # QSize
    size = image.size()
    size.scale(rect.size(), Qt.KeepAspectRatio)  # //此处保证图片显示完整
    painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
    painter.setWindow(image.rect())

    painter.drawPixmap(0, 0, image)  # /* 数据显示至预览界面 */


import sys

app = QApplication(sys.argv)
tablewidget = QTableWidget()
## 设置列数
tablewidget.setColumnCount(4)
tablewidget.horizontalHeader().setDefaultSectionSize(150)

## QStringList在PyQt5
header = ["name", "last modify time", "type", "size"]

tablewidget.setHorizontalHeaderLabels(header)
tablewidget.insertRow(0)
tablewidget.insertRow(0)

pItem1 = QTableWidgetItem("aa")
pItem2 = QTableWidgetItem("bb")
pItem3 = QTableWidgetItem("cc")
pItem4 = QTableWidgetItem("dd")
tablewidget.setItem(0, 0, pItem1)
tablewidget.setItem(0, 1, pItem2)
tablewidget.setItem(0, 2, pItem3)
tablewidget.setItem(0, 3, pItem4)

tablewidget.setMinimumSize(800, 600)

button = QPushButton(u'打印界面')
button.clicked.connect(on_picButton_clicked)

widget = QWidget()
layout = QVBoxLayout(widget)
layout.addWidget(button)
# layout.addWidget(button_txt)
layout.addWidget(tablewidget)
widget.show()

sys.exit(app.exec_())
