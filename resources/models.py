from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Resource(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    publication_date = models.DateTimeField()
    availability = models.TextChoices("2 Days", "10 Days")
    quantity = models.IntegerField()
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE, )
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title
