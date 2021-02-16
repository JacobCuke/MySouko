from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date
from PIL import Image

class Item(models.Model):
    ANIME = 'AN'
    MANGA = 'MA'
    LIGHT_NOVEL = 'LN'
    GAME = 'GM'
    MOVIE = 'MV'
    NOVEL = 'NV'
    DRAMA = 'DR'
    TV_SHOW = 'TV'
    GENRE_CHOICES = [
        (ANIME, 'Anime'),
        (MANGA, 'Manga'),
        (LIGHT_NOVEL, 'Light Novel'),
        (GAME, 'Game'),
        (MOVIE, 'Movie'),
        (NOVEL, 'Novel'),
        (DRAMA, 'Drama'),
        (TV_SHOW, 'TV Series')
    ]

    title = models.CharField(max_length=100)
    cover_art = models.ImageField(default='default.png', upload_to='cover_art_pics')
    series = models.CharField(max_length=100)
    genre = models.CharField(max_length=2, choices=GENRE_CHOICES)
    completed = models.BooleanField(default=False)
    date_started = models.DateField(default=date.today)
    date_completed = models.DateField(default='', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # def save(self):
    #     super().save()

    #     img = Image.open(self.cover_art.path)

    #     if img.width > 300 or img.height > 500:
    #         output_size = (300, 500)
    #         img.thumbnail(output_size)
    #         img.save(self.cover_art.path)

    def get_absolute_url(self):
        return reverse('user-mylist', kwargs={'username': self.user.username})
