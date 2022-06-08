from django.db import models

 
class Investor(models.Model):
    first_name= models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email_addres=models.EmailField(max_length=240,null=True)
    mobile_phone_number=models.CharField(max_length=240,null=True)
    agent_contract=models.CharField(max_length=240,null=True)
    signature=models.ImageField(null=True)
    


    def full_name(self):
        return f"{self.first_name} {self.last_name}"