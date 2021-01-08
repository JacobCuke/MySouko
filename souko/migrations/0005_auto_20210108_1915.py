# Generated by Django 3.1.4 on 2021-01-08 19:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('souko', '0004_auto_20210108_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='date_completed',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='item',
            name='date_started',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
