from django.shortcuts import render, render_to_response
from builtins import locals
from driver import forms
from driver.models import Driver


def index(request):
    pass
    return render(request, 'driver/index.html')


def login(request):
    if request.session.get('is_login', None):
        return render_to_response('driver/index.html')

    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)
        message = '所有的字段都必须填写！'
        if login_form.is_valid():
            user_name = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            # ....
            try:
                user = Driver.objects.get(user_name=user_name)
            except:
                message = '用户不存在'
                return render(request, 'driver/login.html', locals())


            if user.password == password:
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.user_name
                return render_to_response('driver/index.html')
            else:
                message = '密码错误'
                return render(request, 'driver/login.html', locals())
        else:
            return render(request, 'driver/login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'driver/login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        return render_to_response('driver/index.html')

    if request.method == "POST":
        register_form = forms.RegisterForm(request.POST)
        message = '请检查填写的内容!'
        if register_form.is_valid():
            user_name = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            user_num = register_form.cleaned_data['user_num']
            if password1 != password2:
                message = '两次输入的密码不相同！'
                return render(request, 'driver/register.html', locals())
            else:
                same_name_user = Driver.objects.filter(user_name=user_name)
                if same_name_user:
                    message = '用户名已经存在，请重新选择！'
                    return render(request, 'driver/register.html', locals())
                same_email_user = Driver.objects.filter(email=email)
                if same_email_user:
                    message = '该邮箱地址已经被注册，请使用别的邮箱！'
                    return render(request, 'driver/register.html', locals())
                same_email_user_num = Driver.objects.filter(user_num=user_num)
                if same_email_user_num:  # 用户序列号唯一
                    message = '用户序列号已被注册，请使用别的用户序列号！'
                    return render(request, 'driver/register.html', locals())

                user = Driver.objects.create(
                    user_name=user_name,
                    password=password1,
                    email=email,
                    user_num=user_num,
                )

                return render_to_response('driver/index.html')  # 自动跳转到登录页面
            return render(request, 'driver/register.html', locals())
    register_form = forms.RegisterForm()
    return render(request, 'driver/register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return render_to_response("driver/index.html")
    request.session.flush()
    return render_to_response("driver/index.html")

