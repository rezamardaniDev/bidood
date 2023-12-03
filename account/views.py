from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *


# Create your views here.
class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'signup.html', context={'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            exist_user: User & bool = User.objects.filter(email__iexact=form.cleaned_data.get('email')).exists()
            if not exist_user:
                new_user = User()
                new_user.first_name = form.cleaned_data.get('first_name')
                new_user.last_name = form.cleaned_data.get('last_name')
                new_user.email = form.cleaned_data.get('email')
                new_user.phone = form.cleaned_data.get('phone')
                new_user.set_password(form.cleaned_data.get('password'))
                new_user.username = form.cleaned_data.get('email')[0:5]
                new_user.is_staff = False
                new_user.is_superuser = False
                new_user.save()
                return redirect('account:login')
            else:
                form.add_error('email', 'این ایمیل از قبل ثبت نام شده است')
        else:
            form.add_error('confirm_password', 'خطایی در ثبت نام پیش آمده است')

        return render(request, 'signup.html', context={
            'form': form
        })


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', context={'form': form, })

    def post(self, request):
        form = LoginForm(request.POST)
        print(request.POST)
        if form.is_valid():
            user: User & bool = User.objects.filter(email__iexact=form.cleaned_data.get('email')).first()
            if user:
                is_password_correct = user.check_password(form.cleaned_data.get('password'))
                if is_password_correct:
                    login(request, user)
                    return redirect('account:profile')
                else:
                    form.add_error('password', 'رمزعبور وارد شده صحیح نمیباشد')
            else:
                form.add_error('email', 'ابتدا باید در سایت ثبت نام کنید')

        else:
            form.add_error('password', 'مشکلی در ثبت نام پیش آمده است')

        return render(request, 'login.html', context={'form': form})


@login_required(login_url="/account/login")
def logout_user(request):
    logout(request)
    return redirect("bike:bike-list")

@login_required(login_url="/account/login")
def profile(request):
    return render(request, 'profile.html', context={})
