from django import forms
from django.contrib.auth.models import User
from .models import Booking, Food, Order

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class BookingForm(forms.ModelForm):

	class Meta:
		model = Booking
		fields = ['dateBooked', 'timeBooked', 'persons']

class OrderForm(forms.ModelForm):

	class Meta:
		model = Order
		fields = '__all__'