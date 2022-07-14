from email.policy import default
from django.db import models




 
class DataList(models.Model):
    first_name= models.CharField(max_length=240,null=True)
    last_name= models.CharField(max_length=240,null=True)
    email_addres=models.EmailField(max_length=25,null=True,default="your email address")
    city = models.CharField(max_length=50)
    location=models.CharField(max_length=240,null=True,default="Give /sector/district/country")
    phone =models.CharField (max_length=10,null=False,  default="Phone number")
    land_size=models.PositiveSmallIntegerField(null=True,default="hectare")
    price= models.DecimalField(max_digits=10, decimal_places=2)
    zooning_choice=(
        ('R1','R1'),
        ('R1A','R1A'),
        ('R1B','R1B'),
        ('R2','R2'),
        ('R2A','R2A'),
        ('R3','R3'),
        ('R4','R4'),
        ('C1','C1'),
        ('C2','C2'),
        ('C3','C3'),
        ('C3A','C3A'),
        ('C3B','C3B'),
        ('C3C','C3C'),
        ('C4','C4'),
        ('C4A','C4A'),
        ('C5','C5'),
        ('I1','I1'),
        ('I2','I2'),
        ('P1','P1'),
        ('P2','P2'),
        ('P3','P3'),
        ('P4','P4'),
        
    )
    zooning = models.CharField(
        max_length=8, choices=zooning_choice,null=True
    )
    upi_number=models.CharField(max_length=20,null=True)
    down_payment=models.CharField(max_length=240,null=True,default="$")
    how_much_do_you_want_to_invest=models.PositiveIntegerField(null=True)
    signature=models.ImageField(upload_to ='images/',null=True)


    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    

