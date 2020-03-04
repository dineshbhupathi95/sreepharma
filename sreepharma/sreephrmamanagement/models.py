from django.db import models

# Create your models here.
class Userinfromation(models.Model):
    first_name = models.CharField(max_length=300,null=True,blank=True)
    last_name = models.CharField(max_length=300,null=True,blank=True)
    email = models.CharField(max_length=300,null=True,blank=True)
    subject = models.CharField(max_length=300,null=True,blank=True)
    message = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.first_name