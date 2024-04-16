from django.urls import path
from .views import UserRegisterView, UserLoginView
from myapp import views
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('', views.home, name='home'),
]
