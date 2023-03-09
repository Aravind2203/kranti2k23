from django.db import models

# Create your models here.
class Event(models.Model):
    name=models.CharField(max_length=256)
    description=models.TextField(null=True,blank=True)
    rules=models.TextField(null=True,blank=True)
    poster=models.ImageField(null=True,blank=True,upload_to="eventposters")

    def __str__(self):
        return self.name

class Registration(models.Model):
    name=models.CharField(max_length=256,null=True,blank=True)
    number=models.CharField(max_length=10,null=True,blank=True)
    email=models.CharField(max_length=256,null=True,blank=True)
    college=models.CharField(max_length=256,null=True,blank=True)
    event_name=models.CharField(max_length=256,null=True,blank=True)
    year_of_study=models.PositiveIntegerField(null=True,blank=True)
    team_count=models.PositiveIntegerField(null=True,blank=True)
    head_name=models.CharField(max_length=256,null=True,blank=True)
    member_1=models.CharField(max_length=256,null=True,blank=True)
    member_2=models.CharField(max_length=256,null=True,blank=True)
    member_3=models.CharField(max_length=256,null=True,blank=True)

    def __str__(self):
        return str(self.id)

class Sponsords(models.Model):
    name=models.CharField(max_length=256)
    description=models.TextField(null=True,blank=True)
    image=models.ImageField(null=True,blank=True,upload_to="sponsors")
    
