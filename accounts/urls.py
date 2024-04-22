from django.urls import path
from .views import register, user_login, edit_profile, home, user_logout

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('home/', home, name='home'),  # 添加主页路由
    path('logout/', user_logout, name='logout'),
]
