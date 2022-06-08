from email.policy import default
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from location_field.models.plain import PlainLocationField



 
class Land(models.Model):
    first_name= models.CharField(max_length=240,null=True)
    last_name= models.CharField(max_length=240,null=True)
    email_addres=models.EmailField(max_length=240,null=True,default="your email address")
    phone = PhoneNumberField(null=False,  default="Phone number")
    land_size=models.CharField(max_length=240,null=True,default="hectare")
    price= models.DecimalField(max_digits=10, decimal_places=2)
    city = models.CharField(max_length=255)
    zooning=models.CharField(max_length=240,null=True)
    cost_sqm =models.CharField(max_length=240,null=True)
    upi_number=models.CharField(max_length=20,null=True)
    image = models.ImageField()



    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    def __str__(self):
        return str(self.land_size) + ": $" + str(self.price)
