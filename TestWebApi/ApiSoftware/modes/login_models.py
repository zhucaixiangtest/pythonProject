# -*- coding: utf-8

from django.db import models
# Create your models here.



# 用户表
class tbl_user(models.Model):

    user_name = models.TextField(max_length=10)
    email = models.TextField(max_length=50,default='')
    phone=models.CharField(max_length=11,default='')
    password=models.TextField(max_length=30,default='')
    token_value=models.TextField(max_length=100)
    status=models.CharField(max_length=100)
    creat_time = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-creat_time']


# 验证码表
class tbl_verCode(models.Model):
    email = models.TextField(max_length=50, default='')
    phone = models.CharField(max_length=11, default='')
    code=models.TextField(max_length=10, default='')
    status=models.CharField(max_length=3)
    creat_time = models.DateTimeField()
    effective_time=models.DateTimeField()

# 默认倒序
    class Meta:
        ordering = ['-creat_time']



