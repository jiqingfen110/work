# Generated by Django 2.0.5 on 2018-06-05 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_auto_20180605_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='article',
            name='readed_num',
            field=models.IntegerField(default=0),
        ),
    ]
