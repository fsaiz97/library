#import from Model class

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date, timedelta
#from users.models import Profile

class Subject(models.Model):
    subject_name = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.subject_name

class Character(models.Model):
    character_name = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.character_name

class Place(models.Model):
    place_name = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.place_name

class Location(models.Model):
    name = models.CharField(max_length=255, primary_key=True)

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.name

class Resource(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True) # author
    revision = models.PositiveIntegerField() # book edition
    # key = models.CharField(max_length=60, primary_key=True) # Open Library id
    publish_date = models.DateTimeField(null=True, blank=True)
    subjects = models.ManyToManyField(Subject, blank=True) # List of book topics
    characters = models.ManyToManyField(Character, blank=True) # List of book characters
    places = models.ManyToManyField(Place, blank=True) # List of book locations
    quantity = models.PositiveIntegerField(default=1) # Number of books held by the library
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE, ) # The location of the resource within the library

    def __str__(self):
        return self.title



class Loan(models.Model):
    account = models.ForeignKey('users.Profile', related_name='account_loans', on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, related_name='resource_loans', on_delete=models.CASCADE)
    check_out_date = models.DateField(default=timezone.now)
    return_date = models.DateField(null=True,blank=True)
    STATUS_CHOICES = [("D", "Due"),("R","Returned")]
    status = models.CharField(choices=STATUS_CHOICES, default="D", max_length=20)



    #def __str__(self):
    #    return account.username+" has loaned "+resource.title
