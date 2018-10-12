from django.db import models
# from main_app.models import mydevskills

# Create your models here.


class User():
    def __init__(self, name, skill, user_id):
        self.name = name
        self.skill = skill
        self.id = user_id

    def __str__(self):
        return self


class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    skill_level = models.IntegerField()
