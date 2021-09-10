from django.db import models
from django.contrib.auth.models import User
from django.db.models import *
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(default='media/default.jpg', upload_to='profile_pics/', blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def __str__(self):
        return str(self.user)
        
class Anime(models.Model):
    anime_name = models.CharField(max_length=100, blank=True)
    anime_img = models.ImageField(upload_to='anime_img/', blank=True)
    anime_plot = models.TextField(max_length=2000, blank=True)

    def __str__(self):
        return str(self.anime_name)

    @property
    def get_id(self):
        return self.id
        
    
RATE_CHOICES = [
    
    (1, '1 - Horrible'),
    (2, '2 - Bad'),
    (3, '3 - OK'),
    (4, '4 - Good'),
    (5, '5 - Master Piece'),
]


class Reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    text = models.TextField(max_length=2000, blank=True)
    rate = models.IntegerField(choices=RATE_CHOICES, default=1)

    def __str__(self):
        return str(self.user)


