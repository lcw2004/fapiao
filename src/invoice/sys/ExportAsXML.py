# -*- coding: utf-8 -*-

from invoice.common import config
from invoice.common import util


from mako.template import Template

def exportAsStr(invoinceList):
    temp = Template(filename=config.XML_PATH, input_encoding='utf-8', output_encoding='utf-8')
    return temp.render(invoinceList=invoinceList)

def exportAsFile(invoinceList, fileName):
    path = config.INPUT_PATH + fileName
    content = exportAsStr(invoinceList)
    util.saveAsTemp(content, path)
    return util.isFileExists(path)


