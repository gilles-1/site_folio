from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    name = models.fields.CharField(max_length=200)
    title = models.fields.CharField(max_length=200)
    about = models.fields.CharField(max_length=500)
    email = models.EmailField(unique=True)
    telephone = models.fields.CharField(max_length=200)
    city = models.fields.CharField(max_length=200)
    country = models.fields.CharField(max_length=200)
    image = models.ImageField(upload_to='front/src/assets/', blank=True, null=True)
    adresse = models.CharField(max_length=255, blank=True, null=True)
    cv = models.FileField(upload_to='front/public/', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'

class Formation(models.Model):
    class Typ(models.TextChoices):
        Formation = 'Formation'
        Certification = 'Certification'

    typ = models.fields.CharField(choices=Typ.choices, max_length=25)

    name = models.fields.CharField(max_length=300)
    institution = models.fields.CharField(max_length=200)
    city = models.fields.CharField(max_length=50)
    country = models.fields.CharField(max_length=50)
    started_at = models.fields.DateField()
    ended_at = models.fields.DateField()
    in_progress = models.fields.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'

class Skill(models.Model):
    name = models.fields.CharField(max_length=200)
    font_awesome = models.fields.CharField(max_length=200)
    # photo = models.ImageField(upload_to='profile_photo/', blank=True, null=True)
    def __str__(self):
        return f'{self.name}'

class Item(models.Model):
    name = models.fields.CharField(max_length=25)
    skill = models.ForeignKey(Skill, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return f'{self.name}'
    
class Experience(models.Model):

    class Typ(models.TextChoices):
        Emploi = 'Emploi'
        Travail = 'Travail'
        Stage = 'Stage'
        Projet = 'Projet'
        Implication = 'Implication'

    typ = models.fields.CharField(choices=Typ.choices, max_length=25)

    title = models.fields.CharField(max_length=300)
    institution = models.fields.CharField(max_length=50)
    city = models.fields.CharField(max_length=50)
    country = models.fields.CharField(max_length=50)
    started_at = models.fields.DateField()
    ended_at = models.fields.DateField()
    def __str__(self):
        return f'{self.title}'

class Task(models.Model):

    description = models.fields.CharField(max_length=400)
    technology = models.fields.CharField(max_length=55, blank=True, null=True)
    experience = models.ForeignKey(Experience, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return f'{self.description}'
 