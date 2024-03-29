from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):
    country = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    job = models.CharField(max_length=20, default='', blank=True)
    about = models.TextField(max_length=150)  # Assuming it's a TextField for longer text
    candidate_image = models.ImageField(upload_to='profile', null=True, blank=True)
    phone_number = models.CharField(max_length=11, default='', blank=True)

    gender_choices = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    gender = models.CharField(max_length=7, choices=gender_choices, default='male')

    groups = models.ManyToManyField(Group, verbose_name='groups', related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        related_name='custom_user_permissions'
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
