from django.db import models
import inspect

# Create your models here.


class Currency(models.Model):
    currencyname = models.CharField('记账币', max_length=10, unique=True)

    class Meta:
        verbose_name_plural = '币种维护'

    def __str__(self):
        return self.currencyname


class CurrencyRate(models.Model):
    originalcur = models.ForeignKey(
        "Currency",
        on_delete=models.PROTECT,
        related_name='ori_cur')
    originalcur.verbose_name = '原币'
    aftercur = models.ForeignKey(
        "Currency",
        on_delete=models.PROTECT,
        related_name='aft_cur')
    aftercur.verbose_name = '转化币'
    periodrate = models.FloatField('期间汇率')
    pointrate = models.FloatField('即时汇率')
    currencydate = models.DateField('汇率日期')

    class Meta:
        verbose_name_plural = '汇率维护'

    def __str__(self):
        return '%s/%s' % (self.originalcur, self.aftercur)


class BusinessUnit(models.Model):
    buname = models.CharField('板块', max_length=64, unique=True)

    def __str__(self):
        return self.buname

    class Meta:
        verbose_name_plural = '板块维护'


class Company(models.Model):
    companycode = models.CharField(
        "公司编码",
        max_length=64,
        unique=True,
        primary_key=True)
    companyname = models.CharField('公司名', max_length=64)
    parentcompany = models.BooleanField("父级公司", default=True)
    bu = models.ForeignKey('BusinessUnit', on_delete=models.PROTECT, default=1)
    bu.verbose_name = '板块'
    isvalid = models.BooleanField('有效标记', default=True)
    currency = models.ForeignKey(
        'Currency',
        on_delete=models.PROTECT,
        related_name='com_cur',
        default=1)
    currency.verbose_name = '本位币'

    def __str__(self):
        return '%s - %s' % (self.companyname, self.companycode)

    class Meta:
        verbose_name_plural = '公司维护'


class User(models.Model):
    username = models.CharField('用户名', max_length=64)
    password = models.CharField('密码', max_length=256)
    userid = models.CharField('员工号', max_length=10, primary_key=True)
    email = models.EmailField('电子邮件', null=True)
    companycode = models.ForeignKey('Company', on_delete=models.PROTECT)
    companycode.verbose_name = '公司编码'

    class Meta:
        verbose_name_plural = '用户维护'

    def __str__(self):
        return self.username


class AccountType(models.Model):
    typename = models.CharField('科目类别', max_length=64, unique=True)

    class Meta:
        verbose_name_plural = '科目类别维护'

    def __str__(self):
        return self.typename


class AccountBg(models.Model):
    accountid = models.CharField('科目编码', max_length=64, primary_key=True)
    accountname = models.CharField('科目名称', max_length=128)
    parentaccount = models.BooleanField('父级科目', default=False)
    accounttypeid = models.ForeignKey('AccountType', on_delete=models.PROTECT)
    accounttypeid.verbose_name = '科目类别'
    isvalid = models.BooleanField('有效标记', default=True)
    displayname = models.CharField('显示名称', max_length=128, null=True)

    class Meta:
        verbose_name_plural = '科目维护'

    def __str__(self):
        return self.accountname


class Version(models.Model):
    companycode = models.ForeignKey('Company', on_delete=models.PROTECT)
    companycode.verbose_name = '公司编码'
    submittdate = models.DateTimeField('提交日期', auto_now_add=True)
    accountdate = models.DateField('会计期间',)
    isvalid = models.BooleanField('有效标记', default=True)
    versionname = models.CharField(
        '版本ID',
        max_length=64,
        unique=True,
        primary_key=True)
    vaild = models.NullBooleanField('**', default=True)  # 目前此字段停用

    class Meta:
        verbose_name_plural = '版本管理'

    def __str__(self):
        return self.versionname


class ActualData(models.Model):
    version = models.ForeignKey('Version', on_delete=models.CASCADE)
    version.verbose_name = '版本ID'
    accountid = models.ForeignKey('AccountBg', on_delete=models.PROTECT)
    accountid.verbose_name = '科目ID'
    amount = models.FloatField('实际数', blank=False, default=0)

    class Meta:
        unique_together = ('version', 'accountid',)
        verbose_name_plural = '实际发生数'

    def __str__(self):
        return '%s-%s: %s' % (self.version, self.accountid, self.amount)


class BudgetData(models.Model):
    version = models.ForeignKey('Version', on_delete=models.CASCADE)
    version.verbose_name = '版本'
    accountid = models.ForeignKey('AccountBg', on_delete=models.PROTECT)
    accountid.verbose_name = '科目ID'
    amount = models.FloatField('预算数', blank=True, default=0)

    class Meta:
        unique_together = ('version', 'accountid')
        verbose_name_plural = '预算数'


class YtdData(models.Model):
    ytdaccount = models.ForeignKey('AccountBg', on_delete=models.PROTECT)
    ytdaccount.verbose_name = '科目'
    ytdactual = models.FloatField('实际累计', null=False, default=0)
    ytdbudget = models.FloatField('预算累计', null=False, default=0)
    version = models.ForeignKey('Version', on_delete=models.PROTECT)
    version.verbose_name = '版本'

    class Meta:
        verbose_name_plural = '累计数'
        unique_together = ('version', 'ytdaccount',)
