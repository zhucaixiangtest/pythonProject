# Generated by Django 2.0.6 on 2018-07-06 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ApiSoftware', '0012_auto_20180703_2203'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tbl_user',
            options={'ordering': ['-creat_time']},
        ),
        migrations.AlterModelOptions(
            name='tbl_vercode',
            options={'ordering': ['-creat_time']},
        ),
        migrations.RemoveField(
            model_name='tbl_user',
            name='code',
        ),
    ]