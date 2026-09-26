from django import  forms
from django.contrib.auth import  get_user_model

User = get_user_model()

class UserRegisterForm(forms.ModelForm):
    password =forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 =forms.CharField(widget=forms.PasswordInput, label="Confirm_Password")
    class Meta:
        model= User
        fields =['email','username','first_name','last_name']

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('password') != cleaned_data.get('password2'):
            raise forms.ValidationError("Both passwords should be same ")
        return cleaned_data

    def save(self,commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class MyLoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput,label='Password')