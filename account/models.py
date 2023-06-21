from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models


class MyModel(models.Model):
    image = models.ImageField(upload_to='images/')

# Create your models here.


class User(AbstractUser):
    is_admin = models.BooleanField('Is admin', default=False)
    is_patient = models.BooleanField('Is patient', default=False)
    is_doctor = models.BooleanField('Is doctor', default=False)
