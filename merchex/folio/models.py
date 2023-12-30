from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    name = models.fields.CharField(max_length=200)
    title = models.fields.CharField(max_length=200)
    about = models.fields.CharField(max_length=200)
    telephone = models.fields.CharField(max_length=200)
    city = models.fields.CharField(max_length=200)
    country = models.fields.CharField(max_length=200)
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    adresse = models.CharField(max_length=255, blank=True, null=True)
    cv = models.FileField(upload_to='cv/', blank=True, null=True)

    
class Item(models.Model):
    name = models.fields.CharField(max_length=25)

class Formation(models.Model):
    class Type(models.TextChoices):
        Formation = 'Formation'
        Certification = 'Certification'

    type = models.fields.CharField(choices=type.choices, max_length=25)

    name = models.fields.CharField(max_length=200)
    institution = models.fields.CharField(max_length=50)
    city = models.fields.CharField(max_length=50)
    country = models.fields.CharField(max_length=50)
    started_at = models.fields.DateField()
    ended_at = models.fields.DateField()
    in_progress = models.fields.BooleanField(default=False)

class Task(models.Model):

    description = models.fields.CharField(max_length=200)
    technology = models.fields.CharField(max_length=55, blank=True, null=True)

class Skill(models.Model):
    name = models.fields.CharField(max_length=200)
    photo = models.ImageField(upload_to='profile_photo/', blank=True, null=True)
    item = models.ForeignKey(Item, null=True, on_delete=models.SET_NULL)


class Experience(models.Model):

    class Type(models.TextChoices):
        Emploi = 'Emploi'
        Stage = 'Stage'
        Projet = 'Projet'
        Implication = 'Implication'

    type = models.fields.CharField(choices=type.choices, max_length=25)

    title = models.fields.CharField(max_length=200)
    institution = models.fields.CharField(max_length=50)
    city = models.fields.CharField(max_length=50)
    country = models.fields.CharField(max_length=50)
    started_at = models.fields.DateField()
    ended_at = models.fields.DateField()
    task = models.ForeignKey(Task, null=True, on_delete=models.SET_NULL)
 