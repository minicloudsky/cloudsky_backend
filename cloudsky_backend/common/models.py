from django.db import models


class BaseModel(models.Model):
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    update_time = models.DateTimeField(verbose_name="更新时间", auto_now=True)
    is_deleted = models.BooleanField(verbose_name="是否删除", default=False)
    create_by = models.CharField(verbose_name="创建人", max_length=30)
    update_by = models.CharField(verbose_name="更新人", max_length=30)

    class Meta:
        abstract = True
