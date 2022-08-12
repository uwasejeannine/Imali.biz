from email.policy import default
from django.db import models

 
class Developer(models.Model):
    # project=models.ImageField(upload_to ='images/',null=True,)
    steel= models.CharField(max_length=20,default="Kg")
    doors= models.CharField(max_length=20,default="Piece")
    sand= models.CharField(max_length=20,default="Sacks")
    bricks=models.CharField(max_length=240,null=True,default="Number")
    aggregates=models.CharField(max_length=240,null=True,default="Tones")
    stone=models.CharField(max_length=240,null=True,default="Tones")
    window=models.CharField(max_length=16,null=True,default="Piece")
    cement=models.CharField(max_length=240,null=True,default="Sacks")
    glass=models.CharField(max_length=240,null=True,default="Piece")
    metal=models.CharField(max_length=240,null=True,default="Piece")
    woods=models.CharField(max_length=240,null=True,default="Piece")
    
  


    def full_name(self):
        return f"{self.first_name} {self.last_name}"
