#
# listbulk = [['2', 'VBU1100-2020-03-18/37', 'PL010101010101', '123124122142112'], ['3', 'VBU1100-2020-03-18/37', 'PL010101010201', '123123213.34'], ['4', 'VBU1960-2020-03-18/44', 'GBCL', '2323232323'], ['5', 'VBU1960-2020-03-18/44', 'PL0101010104', '1241241242.45'], ['6', 'VBU1960-2020-03-18/44', 'PL0101010106', '2412321321312.45']]
# list = ['2', 'VBU1100-2020-03-18/37', 'PL010101010101', '123124122142112']
#
# rowlist [<ActualData: VBU1100-2020-03-18/37-主营业务收入: 123124122142112>, <ActualData: VBU1100-2020-03-18/37-主营业务成本: 123123213.34>, <ActualData: VBU1960-2020-03-18/44-产量: 2323232323>, <ActualData: VBU1960-2020-03-18/44-销售费用: 1241241242.45>, <ActualData: VBU1960-2020-03-18/44-财务费用: 2412321321312.45>]

import os
import django
import datetime
import time
import inspect
import sys
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "mysite.settings")  # project_name 项目名称
django.setup()
from collector import models, models_view
import pymysql
from openpyxl import load_workbook , Workbook
from openpyxl.styles import PatternFill, Border, Side, Alignment, Protection, Font, colors
import tkinter as tk
from tkinter import filedialog
from dateutil.relativedelta import relativedelta

# obj = models.AccountType.objects.get(typename='费用')
# 用字典的方式逐行写入表记录
# dic ={'id': None, 'typename': '权益'}
# models.AccountType.objects.create(**dic)

# print(models.ActualData.objects.values())
# [{'id': 1, 'version_id': 'VBU1100-2020-03-18/37', 'accountid_id': 'GBCL', 'amount': 10000000.0},
# {'id': 2, 'version_id': 'VBU1100-2020-03-18/37', 'accountid_id': 'PL010101010101', 'amount': 123124122142112.0},
# {'id': 3, 'version_id': 'VBU1100-2020-03-18/37', 'accountid_id': 'PL010101010201', 'amount': 123123213.34},
# {'id': 4, 'version_id': 'VBU1960-2020-03-18/44', 'accountid_id': 'GBCL', 'amount': 2323232323.0},
# {'id': 5, 'version_id': 'VBU1960-2020-03-18/44', 'accountid_id': 'PL0101010104', 'amount': 1241241242.45},
# {'id': 6, 'version_id': 'VBU1960-2020-03-18/44', 'accountid_id': 'PL0101010106', 'amount': 2412321321312.45}]>

# dic1 ={'id': 'None', 'version_id': 'VBU1960-2020-03-18/44', 'accountid_id': 'GBCL', 'amount': '10000000.98'}
# dic2 ={'id': 'None', 'version_id': 'VBU1960-2020-03-18/44', 'accountid_id': 'PL010101010101', 'amount': '1231241212.06'}
# obj1 = models.ActualData(**dic1)
# obj2 = models.ActualData(**dic2)
# list =[obj1,obj2]
# models.ActualData.objects.bulk_create(list)

# fieldlist = []
# for fieldobj in models.ActualData._meta.fields :
#     print(fieldobj.__dict__)
#     fieldlist.append ( fieldobj.__dict__)
# print ( fieldlist )


# for field in models.ActualData._meta.fields :
#
#     print(field)
#     # fields1 = list ( fielddic )
#     # fields2 = list ( fielddic.values () )
#
# # print(fielddic)


# value()和value_list()的差异
valls = models.Currency.objects.values_list() #queryset 成员是一个个列表，通过遍历可取出每个列表元素
val = models.Currency.objects.values() #querset 成员是一个个字典，通过遍历可取出每个字典
print(valls)
print(val)
print(list(valls),list(val)) #把queryset转换成列表
wb = Workbook ()
ws = wb.active
for row in valls:
    ws.append(list(row))
# ws.append(list(tulp))
wb.save('2.xlsx')



# ###### ，判断数据库是否存在某条符合条件的记录方法：
# # 错误写法
# if models.Version.objects.get(versionname='VE1110-2020-03-20/58').DoesNotExist:
#     print('really?')
# else:
#     print('Yes, you are right.')
# print(models.Version.objects.get(versionname='VE1110-2020-03-20/57').DoesNotExist.__doc__)
# print(models.Version.objects.get(versionname='VE1110-2020-03-20/57').DoesNotExist)
# print(type(models.Version.objects.get(versionname='VE1110-2020-03-20/57')))
# # 正确写法：
# from django.core.exceptions import ObjectDoesNotExist
# try:
#     e = models.Version.objects.get(versionname='VE1110-2020-03-20/57')
#     b = models.Version.objects.get(versionname='VE1110-2020-03-20/61')
# except ObjectDoesNotExist:
#     print("Either the entry or blog doesn't exist.")

