from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.views import View
from django.contrib.auth.forms import UserCreationForm
import os
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user







class MyLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

    def __init__(self, *args, **kwargs):
        super(MyLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Username"
        self.fields['password'].label = "Password"









class UserRegisterView(View):
    template_name = 'myapp/register.html'
    form_class = MyRegistrationForm
    
    def get(self, request, *args, **kwargs):
        
        form = self.form_class()
        # 这里你把表单传给了模板
        return render(request, self.template_name, {'form': form})
        
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)  # 使用提交的数据创建一个表单实例
        if form.is_valid():  # 检查表单数据是否有效
            user = form.save(commit=False)  # 保存用户模型实例，但暂时不提交到数据库
            user.save()  # 现在将用户数据保存到数据库
            # 你可以在这里添加额外的逻辑，比如发送欢迎邮件或者重定向到登录页面
            return JsonResponse({"message": "User registered successfully"}, status=201)  # 返回成功的JSON响应
        else:
            # 如果表单无效，返回错误信息的JSON响应
            return JsonResponse({"errors": form.errors}, status=400)


from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.views import View
from django import forms

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserLoginView(View):
    template_name = 'myapp/login.html'
    form_class = MyLoginForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()  # 初始化表单
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # 尝试使用表单提供的凭证进行认证
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)  # 登录用户
                return JsonResponse({"message": "Login successful"}, status=200)
            else:
                # 认证失败，返回错误信息
                return JsonResponse({"error": "Invalid credentials"}, status=400)
        else:
            # 表单数据无效，返回错误信息
            print(form.errors)
            return JsonResponse({"errors": form.errors}, status=400)



# 引入HttpResponse模块
from django.http import HttpResponse

# 定义home视图
def home(request):
    # 返回一个包含欢迎信息的HTTP响应
    return HttpResponse("<h1>Welcome to My Django App!</h1>")




