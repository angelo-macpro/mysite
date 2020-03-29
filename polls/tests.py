import os
import django
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "mysite.settings")  # project_name 项目名称
django.setup()
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from polls.models import Question, Choice
from django.test import TestCase

# Create your tests here.


print(Question.objects.all())
# q = Question(question_text="What's new?", pub_date=timezone.now()) #新建一条记录,和.save配对使用
# q.save()
q = Question.objects.get(id=1)
print(q.question_text)
print(q.pub_date)
print(Question.objects.all())
print(Question.objects.filter(question_text__startswith='What'))
# print(Question.objects.get(pub_date__year=timezone.now().year ))
q = Question.objects.get(pk=1)
print(q.was_published_recently())

# print(q.choice_set.all)  #一对多关联查询，先找出一，然后把多的表名不大写开头加上'_set'
# 如果嫌麻烦就用related_name,在models里定义好，但一旦用了上述表名小写加set的方法即失效
print(q.question_choice.all)

# q.question_choice.create(choice_text='The Sky', votes=0)   #是不是可以用add批量增加？
#  q.question_choice.create(choice_text='Just Hacking Again', votes=0)
# q.question_choice.create(choice_text='科洛娜病毒', votes=0)
c = q.question_choice.get(pk=3)  # 从Question关联查询到Choice
print(c.question)
current_year = timezone.now().year
print(q.question_choice.all())
print(q.question_choice.count())
print(Choice.objects.filter(question__pub_date__year=current_year))

# 如果有不存在的记录，就唤醒DoesNotExit例外事项
try:
    Choice.objects.get(id=3)
except ObjectDoesNotExist:
    print('不存在')


# c = q.question_choice.filter(choice_text__startswith='Just')
# c.delete()  #add(), create(), remove(), clear(), and set()
# 都是关联表中可用的函数，不仅适用于多对一，还有多对多(后续深入点***)


