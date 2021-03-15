from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class UserProfile(AbstractUser):
    gender_choices = (
        ('male', '男'),
        ('female', '女')
    )

    status_choices = (
        ('active', '可用'),
        ('locked', '锁定'),
        ('deleted', '已删除')
    )
    password = models.CharField(_('password'), max_length=128, null=True, blank=True)
    name = models.CharField('昵称', max_length=50, default='', null=True)
    birthday = models.DateField('生日', null=True, blank=True)
    sex = models.CharField('性别', max_length=10, choices=gender_choices, default='female', null=True)
    adress = models.CharField('地址', max_length=100, default='')
    phone = models.CharField('手机号', max_length=11, null=True, blank=True)
    is_active = models.BooleanField('用户状态', default=True)
    image = models.CharField('头像', max_length=300, null=True)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    update_time = models.DateTimeField(verbose_name="更新时间", auto_now=True)
    create_by = models.CharField(verbose_name="创建人", max_length=30)
    update_by = models.CharField(verbose_name="更新人", max_length=30)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
