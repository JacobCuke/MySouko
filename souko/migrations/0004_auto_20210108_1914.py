# Generated by Django 3.1.4 on 2021-01-08 19:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('souko', '0003_auto_20210108_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='date_completed',
            field=models.DateField(default=datetime.date(2021, 1, 8)),
        ),
        migrations.AlterField(
            model_name='item',
            name='date_started',
            field=models.DateField(default=datetime.date(2021, 1, 8)),
        ),
    ]