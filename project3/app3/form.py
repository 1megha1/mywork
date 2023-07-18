from.models import register
from django import forms
class registerform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput,max_length=10,min_length=2)
    confirmpassword=forms.CharField(widget=forms.PasswordInput,max_length=10,min_length=2)
    class Meta:
        model=register
        fields='__all__'
class LoginForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput,max_length=10,min_length=2)
    class Meta:
        model = register
        fields=('email',)
class Updateform(forms.ModelForm):
    class Meta():
        model=register
        fields=('name','age','place','email')
class changepasswordForm(forms.Form):
    OldPassword=forms.CharField(widget=forms.PasswordInput,max_length=10,min_length=2)
    NewPassword=forms.CharField(widget=forms.PasswordInput,max_length=10,min_length=2)
    ConfirmPassword=forms.CharField(widget=forms.PasswordInput,max_length=10,min_length=2)
