from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
# Create your models here.

class CustomUser(AbstractUser):
    google_id = models.BigIntegerField(unique=True, null = True)
    profile_image = models.TextField(default="", null = True)
    groups = models.ManyToManyField(Group, related_name='custom_users')
    
    # 권한 관계에 대한 related_name 지정
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users')