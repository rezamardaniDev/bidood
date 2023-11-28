from django.shortcuts import render, redirect
from django.views.generic import View

from .forms import *
from .models import *


# Create your views here.
class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'signup.html', context={
            'form': form,
        })

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            exist_user: User & bool = User.objects.filter(email__iexact=form.cleaned_data.get('email')).exists()
            if not exist_user:
                new_user = User()
                new_user.first_name = form.cleaned_data.get('first_name')
                new_user.last_name = form.cleaned_data.get('last_name')
                new_user.email = form.cleaned_data.get('email')
                new_user.set_password(form.cleaned_data.get('password'))
                new_user.is_staff = False
                new_user.is_superuser = False
                new_user.save()
                return redirect()
            else:
                form.add_error('email', 'این ایمیل از قبل ثبت نام شده است')
        else:
            form.add_error('confirm_password', 'خطایی در ثبت نام پیش آمده است')

        return render(request, 'seccess_signup.html', context={
            'from': form
        })


class LoginView(View):
    ...

def seccess_signup(request):
    return render(request, 'seccess_signup.html', context={})

def failure_signup(request):
    return render(request, 'failure_signup.html', context={})