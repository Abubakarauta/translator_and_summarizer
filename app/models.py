from django.db import models
from django.contrib.auth.models import User

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=50, default='', blank=True)
    country = models.CharField(max_length=50, default='', blank=True)
    address = models.CharField(max_length=50, default='', blank=True)
    job = models.CharField(max_length=20, default='', blank=True)
    about = models.TextField(max_length=150, default='', blank=True)
    candidate_image = models.ImageField(upload_to='profile', null=True, blank=True)
    phone_number = models.CharField(max_length=255, blank=True, default='')
    email = models.EmailField(max_length=50, default='')  # Example email field
    twitter = models.CharField(max_length=255, blank=True, default='')
    facebook = models.CharField(max_length=255, blank=True, default='')
    instagram = models.CharField(max_length=255, blank=True, default='')
    linkedin = models.CharField(max_length=255, blank=True, default='')
    first_name = models.CharField(max_length=30, blank=True, default='')  # Add first_name field
    last_name = models.CharField(max_length=30, blank=True, default='')  # Add last_name field

    gender_choices = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    gender = models.CharField(max_length=7, choices=gender_choices, default='male')

    def __str__(self):
        return self.user.username
