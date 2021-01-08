# Generated by Django 3.1.4 on 2021-01-08 19:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('cover_art', models.ImageField(default='default.png', upload_to='cover_art_pics')),
                ('series', models.CharField(max_length=100)),
                ('genre', models.CharField(choices=[('AN', 'アニメ'), ('MA', '漫画'), ('LN', 'ライトノベル'), ('GM', 'ゲーム')], max_length=2)),
                ('status', models.BooleanField(default=False)),
                ('date_started', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_completed', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]