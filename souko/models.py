from django.db import models
from datetime import date
from PIL import Image

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

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.width > 300 or img.height > 500:
            output_size = (300, 500)
            img.thumbnail(output_size)
            img.save(self.image.path)
