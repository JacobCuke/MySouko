# Generated by Django 3.1.4 on 2021-01-08 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('souko', '0006_auto_20210108_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='date_completed',
            field=models.DateField(blank=True, default='', null=True),
        ),
    ]
