from email.policy import default
from django.db import models

 
class Developer(models.Model):
    project=models.ImageField(null=True)
    steel= models.CharField(max_length=20)
    doors= models.CharField(max_length=20)
    sand= models.CharField(max_length=20)
    bricks=models.CharField(max_length=240,null=True)
    aggregates=models.CharField(max_length=240,null=True)
    stone=models.CharField(max_length=240,null=True)
    window=models.CharField(max_length=16,null=True)
    cement=models.CharField(max_length=240,null=True)
    glass=models.CharField(max_length=240,null=True)
    metal=models.CharField(max_length=240,null=True)
    woods=models.CharField(max_length=240,null=True)
    
  


    def full_name(self):
        return f"{self.first_name} {self.last_name}"
