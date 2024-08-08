from django.db import models
from django.utils import timezone

# Create your models here.

class Members(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    fee_amount = models.IntegerField()
    fee_date = models.DateField(default=timezone.now)
    image = models.ImageField(upload_to='members/')
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
