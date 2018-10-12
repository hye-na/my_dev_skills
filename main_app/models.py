from django.db import models

# Create your models here.


class User():
    def __init__(self, name, skill):
        self.name = name
        self.skill


class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    skill_level = models.IntegerField()
