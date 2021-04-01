from django.db import models
from django.contrib.auth import get_user_model
#from resources.models import Resource, Loan


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    loans = models.ManyToManyField('resources.Resource', through='resources.Loan')

    def __str__(self):
        return f'{self.user.username} Profile'