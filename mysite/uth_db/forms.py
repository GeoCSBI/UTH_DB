from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):

	password = forms.CharField(widget=froms.PasswordInput)

	class Meta:
		model = User
		field = ['username', 'email', 'password']