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


# #Django models之related_name 和 _set,不可同时并存，但均适用于"一查询多"
# # 通过币种查询适用该币种的所有公司
# cny = models.Currency.objects.get(currencyname__contains='CNY')
# # print(cny.company_set.all()) #一旦在Foreykey中定义了related_name，此项命令即失效
# print(cny.comp_cur.all())
#
# # 没有定义related_name，则可用：（通过科目类型查询属于该科目类型的所有科目）
# accountgroup = models.AccountType.objects.get(typename='费用')
# print(accountgroup.account_set.all())


# 从models到数据库，从类到表和视图，再到excel的sheet和field，思路历程：
# print(models)
# print(dir(models))
# print(models.__name__)
# print(models.AccountBg.__str__)
# print(dir(models.AccountBg))
# print(models.AccountBg.__dict__)
# print(models.AccountBg.__name__)
# #取出表的中文名
# print(models.AccountBg._meta.verbose_name_plural)
#
# #取出字段的中文名
# fielddic1={}
# for field1 in models.AccountBg._meta.fields:
#     fielddic1[field1.name] = field1.verbose_name
# print(fielddic1)
#
# for name, obj in inspect.getmembers(sys.modules[__name__]):
#     if inspect.isclass(obj):
#         print(obj)
#         print(name)
#
# # 获取openpyxl类中所有方法列表：
# method_list1 = [func for func in dir(Protection) if callable(getattr(Protection, func))]
# print(len(method_list1))
# # 排除内置方法列表：
# method_list2 = [func for func in dir(Protection) if callable(getattr(Protection, func)) and not func.startswith("__")]
# print(method_list2)
#
# i = 0
# for method in inspect.getmembers(Protection):
#     print(method)
#     i = i+1
#     print(i)

from django.contrib import admin
from django.urls import path,include
print(type(django))
print(type(django.contrib.admin))
print(path.__dir__)
print(include.__dir__)

print(type(models))

