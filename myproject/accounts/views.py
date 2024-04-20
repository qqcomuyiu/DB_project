from django.shortcuts import render

# Create your views here.
# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, LoginForm
from django.contrib.auth import logout
from django.shortcuts import render
from django.contrib import messages  # 引入 Django 的消息框架


def home(request):
    return render(request, 'accounts/home.html')


def user_logout(request):
    logout(request)
    return redirect('login')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                print(11)
                if user.is_active:  # 检查用户是否被激活
                    login(request, user)
                    return redirect('home')
                else:
                    messages.error(request, "Your account is disabled.")  # 用户被禁用的情况
            else:
                messages.error(request, "Invalid username or password.")  # 认证失败的情况
        else:
            messages.error(request, "Invalid username or password.")  # 表单数据无效的情况
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})
