# Generated by Django 2.0.6 on 2018-07-02 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiSoftware', '0005_auto_20180702_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_user',
            name='creat_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
