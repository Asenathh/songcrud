from django.db import models

# Create your models here.

class Artist(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name

class Song(models.Model):
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    date_released = models.DateField(auto_now=True)
    likes = models.IntegerField()

    def __str__(self):
        return self.title

class Lyric(models.Model):
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000)

    def __str__(self):
        return self.content
