# Generated by Django 3.1.4 on 2021-02-16 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('souko', '0009_auto_20210215_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='cover_art',
            field=models.ImageField(default='default.png', upload_to='cover_art_pics'),
        ),
    ]
