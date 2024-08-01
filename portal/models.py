from django.db import models

# Create your models here.

class Members(models.Model):
    name = models.CharField(max_length=255),
    phone_number = models.CharField(max_length=255),
    fee_amount = models.IntegerField(max_length=55),
    fee_date = models.DateField(auto_now_add=True),
    image = models.ImageField(upload_to='members/'),
    state = models.BooleanField(default=True),
    
    def __str__(self):
        return self.name + "added in portal successfully."