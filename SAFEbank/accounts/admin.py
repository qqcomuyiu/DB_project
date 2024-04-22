from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User

# 注册你的模型
admin.site.register(User)
