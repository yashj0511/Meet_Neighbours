from django.db import models

# Create your models here.



class Person(models.Model):
    Firstname = models.CharField(max_length=100,null=False,blank=False)
    Lastname=models.CharField(max_length=100,null=False,blank=False)
    MiddleName=models.CharField(max_length=100,null=True,blank=True)
    Age=models.IntegerField(null=True)
    Profile_Pic=models.ImageField(null=True,upload_to='ConnectNeighbours/images')
    GENDER_CHOICES = [
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),
        
    ]
    Gender = models.CharField(max_length=6,choices=GENDER_CHOICES,null=True)
    Address=models.TextField(blank=False,null=False)
    val= [
        ('Available','Available'),
        ('Busy','Busy')
    ]
    Status=models.CharField(max_length=9,choices=val)


    