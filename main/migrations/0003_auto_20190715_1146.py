# Generated by Django 2.2.2 on 2019-07-15 11:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190715_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 15, 11, 46, 53, 836674), verbose_name='date published'),
        ),
    ]