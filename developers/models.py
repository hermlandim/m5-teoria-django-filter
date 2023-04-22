from django.db import models


class ExperienceChoice(models.TextChoices):
    JR = "Junior"
    PL = "Pleno"
    SN = "Senior"


class Developer(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    state = models.CharField(max_length=30)
    favorite_language = models.CharField(max_length=20)
    experience = models.CharField(max_length=20, choices=ExperienceChoice.choices, default=ExperienceChoice.JR)
