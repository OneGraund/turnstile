from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=80, blank=False)
    last_name = models.CharField(max_length=80, blank=False)
    email = models.EmailField()
    phone = models.PhoneField()
    grade = models.IntegerField(blank=False)

