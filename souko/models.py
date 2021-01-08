from django.db import models
from datetime import date

class Item(models.Model):
    ANIME = 'AN'
    MANGA = 'MA'
    LIGHT_NOVEL = 'LN'
    GAME = 'GM'
    GENRE_CHOICES = [
        (ANIME, 'アニメ'),
        (MANGA, '漫画'),
        (LIGHT_NOVEL, 'ライトノベル'),
        (GAME, 'ゲーム'),
    ]

    title = models.CharField(max_length=100)
    cover_art = models.ImageField(default='default.png', upload_to='cover_art_pics')
    series = models.CharField(max_length=100)
    genre = models.CharField(max_length=2, choices=GENRE_CHOICES)
    completed = models.BooleanField(default=False)
    date_started = models.DateField(default=date.today)
    date_completed = models.DateField(default=date.today)

    def __str__(self):
        return self.title
