from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .forms import RegisterUserForm, CustomPasswordResetForm
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordResetDoneView
from django.contrib import messages


def base(request):
    return render(request, 'base.html')


def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        form = RegisterUserForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


def password_reset_view(request):
    if request.method == 'POST':
        form = CustomPasswordResetForm(request.POST)
        if form.is_valid():
            form.save(request=request)
            messages.success(request, 'Письмо с инструкциями по сбросу пароля отправлено на вашу электронную почту.')
    else:
        form = CustomPasswordResetForm()
    return render(request, 'password_reset_view.html', {'form': form})


class CustomPasswordResetView(PasswordResetView):
    template_name = 'password_reset_view.html'
    form_class = CustomPasswordResetForm
    success_url = '/password-reset/done/'

    def form_valid(self, form):
        form.save(request=self.request)
        messages.success(self.request, 'Письмо с инструкциями по сбросу пароля отправлено на вашу электронную почту.')
        return super().form_valid(form)

    def get_success_url(self):
        return '/password-reset/done/'



class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'password_reset_complete.html'


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'password_reset_done.html'
