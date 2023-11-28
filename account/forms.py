from django import forms


class LoginForm(forms.Form):
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