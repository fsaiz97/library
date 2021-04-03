from django.db import models
from django.contrib.auth import get_user_model
#from resources.models import Resource, Loan
from rest_framework.response import Response
from django.db.models.signals import post_save
from django.dispatch import receiver
#from django.contrib.auth import get_user_model


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    loans = models.ManyToManyField('resources.Resource', through='resources.Loan')

    def __str__(self):
        return f'{self.user.username} Profile'


@receiver(post_save, sender=get_user_model())
def createProfile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
