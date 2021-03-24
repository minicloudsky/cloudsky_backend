# Generated by Django 3.1.7 on 2021-03-24 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApiLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_name', models.CharField(max_length=200, verbose_name='接口名')),
                ('method', models.CharField(max_length=20, verbose_name='请求方法')),
                ('param', models.TextField(blank=True, max_length=5000, null=True, verbose_name='请求参数')),
                ('comment', models.CharField(blank=True, max_length=255, null=True, verbose_name='备注')),
                ('time', models.BigIntegerField(verbose_name='执行时长(毫秒)')),
                ('ip', models.CharField(max_length=64, verbose_name='IP地址')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('username', models.CharField(max_length=30, verbose_name='访问用户名')),
                ('status_code', models.CharField(max_length=10, verbose_name='状态码')),
                ('status_text', models.CharField(max_length=30, verbose_name='状态说明')),
            ],
            options={
                'verbose_name': 'api访问日志',
                'verbose_name_plural': 'api访问日志',
            },
        ),
    ]
