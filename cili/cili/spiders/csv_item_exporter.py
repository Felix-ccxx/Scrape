# -*- coding: utf-8 -*-
"""
Created on Wed Apr 05 13:02:33 2017

@author: Administrator
"""

'''
在spiders目录中增加文件csv_item_exporter.py
Scrapy官方文档“Item Exporters”一节
'''

#Import配置和相应导出文件格式的Item输出器
from scrapy.conf import settings
from scrapy.contrib.exporter import CsvItemExporter

#类名可自定义修改，但要同步修改setting.py
class CiliCsvItemExporter(CsvItemExporter):

    def __init__(self, *args, **kwargs):
        delimiter = settings.get('CSV_DELIMITER', ',')
        kwargs['delimiter'] = delimiter

		#FIELDS_TO_EXPORT与setting.py中相匹配
        fields_to_export = settings.get('FIELDS_TO_EXPORT', [])
        if fields_to_export :
            kwargs['fields_to_export'] = fields_to_export

        super(CiliCsvItemExporter, self).__init__(*args, **kwargs)