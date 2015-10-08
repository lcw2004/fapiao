# -*- coding: utf-8 -*-

from invoice.common import config


from mako.template import Template

def getMailHtml(invoinceList):
    mytemplate = Template(filename=config.XML_PATH, input_encoding='utf-8', output_encoding='utf-8')
    return mytemplate.render(invoinceList=invoinceList)

