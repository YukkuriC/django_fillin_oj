from django.db import models
from usr_sys.models import User
from main import settings


class Problem(models.Model):
    title = models.CharField('题目', max_length=128)
    descrip = models.TextField('题目描述')
    struct = models.TextField('代码结构')

    class Meta:
        verbose_name = "题目"
        verbose_name_plural = "题目"


class TestCase(models.Model):
    problem = models.ForeignKey(Problem, models.CASCADE, verbose_name='题目')
    index = models.CharField('编号', max_length=4)
    time_limit = models.FloatField('')
    stdin = models.TextField('输入')
    stdout = models.TextField('输出')

    class Meta:
        ordering = ["problem__id"]
        verbose_name = "测试点"
        verbose_name_plural = "测试点"


class Submission(models.Model):
    user = models.ForeignKey(User, models.CASCADE, verbose_name='用户')
    problem = models.ForeignKey(Problem, models.CASCADE, verbose_name='题目')
    time = models.DateTimeField('提交时间', auto_now_add=True)
    content = models.TextField('提交内容')
    status = models.SmallIntegerField('状态', choices=settings.SUBMISSION_STATUS)
    time = models.IntegerField('用时')
    detail = models.TextField('细节')

    class Meta:
        ordering = ["-id"]
        verbose_name = "提交"
        verbose_name_plural = "提交"
