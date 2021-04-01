from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Profile

@reciever(post_save, sender=get_user_model())
def createProfile(sender, instance, created, **kwargs):
    return Response("testing",status=420)
    if created:
        Profile.objects.create(user=instance)