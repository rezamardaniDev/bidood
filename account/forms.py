from django import forms


class SignUpForm(forms.Form):
    first_name = forms.CharField(
        label='نام',
        widget=forms.TextInput()
    )
    last_name = forms.CharField(
        label='نام خانوادگی',
        widget=forms.TextInput()
    )
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput()
    )
    phone = forms.CharField(
        label='شماره تماس',
        widget=forms.TextInput()
    )
    password = forms.CharField(
        label="پسورد",
        widget=forms.TextInput()
    )
    confirm_password = forms.CharField(
        label="تکرار پسورد",
        widget=forms.TextInput()
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return confirm_password
        else:
            raise forms.ValidationError("رمز عبور های وارد شده یکسان نیستند")

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        if len(phone) > 11:
            raise forms.ValidationError("شماره تلفن معتبر نمیباشد")
        else:
            return phone


class LoginForm(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(),
        error_messages={
            'required': 'ایمیل خود را وارد کنید'
        }
    )
    password = forms.CharField(
        label='پسورد',
        widget=forms.TextInput(),
        error_messages={
            'required': 'پسورد خود را وارد کنید'
        }
    )
