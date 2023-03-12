from django.db import models

# Create your models here.
class Event(models.Model):
    name=models.CharField(max_length=256)
    description=models.TextField(null=True,blank=True)
    rules=models.TextField(null=True,blank=True)
    poster=models.ImageField(null=True,blank=True,upload_to="eventposters")

    def __str__(self):
        return self.name
class FifaRegistration(models.Model):
    email=models.CharField(max_length=256,null=True,blank=True)
    team_name=models.CharField(max_length=256,null=True,blank=True)
    college_name=models.CharField(max_length=256,null=True,blank=True)
    member1=models.CharField(max_length=256,null=True,blank=True)
    member2=models.CharField(max_length=256,null=True,blank=True)
    phone1=models.CharField(max_length=10,null=True,blank=True)
    phone2=models.CharField(max_length=10,null=True,blank=True)
    event=models.CharField(max_length=256,null=True,blank=True)
    year_of_study=models.PositiveIntegerField(null=True,blank=True)
    payment_image=models.ImageField(null=True,blank=True,upload_to="fifa/")

    def __str__(self):
        return str(self.id)
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
    

class CodRegistration(models.Model):
    team_name=models.CharField(max_length=256,null=True,blank=True)
    lead_name=models.CharField(max_length=256,null=True,blank=True)
    lead_ph_no=models.CharField(max_length=256,null=True,blank=True)
    mem2=models.CharField(max_length=256,null=True,blank=True)
    mem3=models.CharField(max_length=256,null=True,blank=True)
    email=models.CharField(max_length=256,null=True,blank=True)
    event_name=models.CharField(max_length=50,null=True,blank=True)
    year=models.PositiveIntegerField(null=True,blank=True)
    payment=models.ImageField(null=True,blank=True,upload_to="cod/")
    college_name=models.CharField(max_length=256,null=True,blank=True)

    

    def __str__(self):
        return str(self.id)

class ValoRegistration(models.Model):
    teamname=models.CharField(max_length=256,null=True,blank=True)
    leadname=models.CharField(max_length=256,null=True,blank=True)
    leadnumber=models.CharField(max_length=256,null=True,blank=True)
    riotid=models.CharField(max_length=256,null=True,blank=True)
    discordid=models.CharField(max_length=256,null=True,blank=True)
    mem2=models.CharField(max_length=256,null=True,blank=True)
    mem2ph=models.CharField(max_length=256,null=True,blank=True)
    mem2dis=models.CharField(max_length=256,null=True,blank=True)
    mem3=models.CharField(max_length=256,null=True,blank=True)
    #mem2ph=models.CharField(max_length=256,null=True,blank=True)
    mem3dis=models.CharField(max_length=256,null=True,blank=True)
    mem4=models.CharField(max_length=256,null=True,blank=True)
    mem4dis=models.CharField(max_length=256,null=True,blank=True)
    mem5=models.CharField(max_length=256,null=True,blank=True)
    mem5dis=models.CharField(max_length=256,null=True,blank=True)
    email=models.CharField(max_length=256,null=True,blank=True)
    college_name=models.CharField(max_length=256,null=True,blank=True)
    event_name=models.CharField(max_length=256,null=True,blank=True)
    year=models.PositiveBigIntegerField(null=True,blank=True)
    payment=models.ImageField(null=True,blank=True,upload_to="valo/")

    def __str__(self) -> str:
        return str(self.id)