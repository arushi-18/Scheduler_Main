from django import forms
from .models import User,Profile
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
	email=forms.EmailField()
	class Meta:
		model=User
		fields=['email','username','password1','password2']

class UserUpdateForm(forms.ModelForm):
	#email=forms.EmailField()
	class Meta:
		model=User
		fields=['username']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model=Profile
		fields=['image']