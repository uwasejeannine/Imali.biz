from email.policy import default
from django.db import models

 
class Buyer(models.Model):
    first_name= models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email_addres=models.EmailField(max_length=240,null=True)
    phone_number=models.CharField(max_length=240,null=True)
    agent_contract=models.CharField(max_length=240,null=True)
    your_id=models.CharField(max_length=16,null=True,default="your national id number")
    down_payment=models.CharField(max_length=240,null=True,default="$")
    signature=models.ImageField(null=True)
    
  


    def full_name(self):
        return f"{self.first_name} {self.last_name}"