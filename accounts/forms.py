from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import UserProfile


class ExtendedUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'username')

    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']

        if commit:
            user.save()
        return user

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone',)
