from django.db import models
from django.contrib.auth.models import User

class Character(models.Model):
    portraits = (
        ('1','Fighter'),
        ('2','Wizard'),
        ('3','Rogue'),
        ('4','Cleric'), 
        ('5','Druid'),
        ('6','Paladin'),
        ('7','Barbarian'),
        ('8','Ranger'),
        ('9','Bard'),
        ('10','Monk'),
        ('11','Sorcerer'),
        ('12','Warlock')
        )
    name = models.CharField(max_length=16)
    race = models.CharField(max_length=16)
    classes = models.CharField(max_length=16)
    background = models.CharField(max_length=16)
    alignment = models.CharField(max_length=16)
    strength = models.IntegerField()
    dexterity = models.IntegerField()
    constitution = models.IntegerField()
    intelligence = models.IntegerField()
    wisdom = models.IntegerField()
    carisma = models.IntegerField()
    hitpoints = models.IntegerField()
    level = models.IntegerField()
    image = models.CharField(blank=True, max_length=100, choices=portraits)
    description = models.TextField(blank=True)
    inventory = models.TextField(blank=True)
    player = models.ForeignKey(User, on_delete=models.CASCADE, related_name='character',null=True)
    
    def __str__(self):
        return self.name
