from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms

class UserRegistrationForm(ModelForm):
    password_confirm = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', ]
        widgets = { 'password': forms.PasswordInput() }

    def clean(self):
        cleaned_data = super(UserRegistrationForm, self).clean()
        if cleaned_data['password'] != cleaned_data['password_confirm']:
            raise forms.ValidationError("Password and Confirm Password have to be the same")

        return cleaned_data

    def save(self):
        del self.cleaned_data['password_confirm']
        return User.objects.create_user(**self.cleaned_data)


