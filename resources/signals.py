from django.db.models.signals import post_save
from django.dispatch import reciever
from .models import Loan

@reciever(post_save, sender=Loan)
def update_quantity(instance, **kwargs):
    # print("before ",instance.resource.quantity)
    if instance.resource.quantity == 0:
        pass
    else:
        instance.resource.quantity -=1
        instance.resource.save()