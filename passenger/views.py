from builtins import locals
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from passenger import forms
from passenger.models import Passenger
from django.views.decorators.csrf import csrf_exempt
from hashlib import sha256
import json

# def hash_code(string, salt='python'):
#     h = sha256(string.encode()+salt.encode())
#     return h.hexdigest()


def login(request):
    if request.session.get('is_login', None):
        return render_to_response('passenger/login.html')

    if request.method == "POST":
        login_form = forms.UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            user_name = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = Passenger.objects.get(user_name=user_name)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.user_name
                    return render_to_response('passenger/accounts_profile.html')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'passenger/login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'passenger/login.html', locals())



def register(request):
    if request.session.get('is_login', None):
        return render_to_response("passenger/index.html")

    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        message = '请检查填写的内容'
        if register_form.is_valid():
            user_name = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            user_num = register_form.cleaned_data['user_num']
            if password1 != password2:
                message = '两次输入的密码不同'
                return render(request, 'passenger/register.html', locals())
            else:
                same_name_user = Passenger.objects.filter(user_name=user_name)
                if same_name_user:
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'passenger/register.html', locals())
                same_email_user = Passenger.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'passenger/register.html', locals())
                same_email_user_num = Passenger.objects.filter(user_num=user_num)
                if same_email_user_num:  # 用户序列号唯一
                    message = '用户序列号已被注册，请使用别的用户序列号！'
                    return render(request, 'passenger/register.html', locals())

                # 当一切都OK的情况下，创建新用户
                user = Passenger.objects.create(
                    user_name=user_name,
                    password=password1,
                    email=email,
                    sex=sex,
                    user_num=user_num,
                )

                return render_to_response('passenger/login.html')  # 自动跳转到登录页面
            return render(request, 'passenger/register.html', locals())
    register_form = forms.RegisterForm()
    return render(request, 'passenger/register.html', locals())

def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return render_to_response("passenger/login.html")
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return render_to_response("main/base.html")

def accounts_profile(request):
    # if request.method == 'POST':
    #     a = json.loads(request.body)
    #     print(a)
    #     b = Passenger.objects.get(email=request.user.email)
    #     b.name = a['name']
    #     b.sex = a['sex']
    #     b.birthday = a['birthday']
    #     b.live_place = a['live_place']
    #     b.phone = a['phone']
    #     b.save()
    return render(request, 'passenger/accounts_profile.html')
