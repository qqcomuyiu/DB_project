
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # 可以添加额外的字段
    bio = models.TextField(null=True, blank=True)

