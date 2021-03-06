# Generated by Django 3.1.4 on 2021-02-15 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('souko', '0008_item_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='cover_art',
            field=models.ImageField(blank=True, default='default.png', upload_to='cover_art_pics'),
        ),
        migrations.AlterField(
            model_name='item',
            name='genre',
            field=models.CharField(choices=[('AN', 'Anime'), ('MA', 'Manga'), ('LN', 'Light Novel'), ('GM', 'Game'), ('MV', 'Movie'), ('NV', 'Novel'), ('DR', 'Drama'), ('TV', 'TV Series')], max_length=2),
        ),
    ]
