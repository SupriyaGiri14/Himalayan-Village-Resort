from statistics import mode
from tabnanny import check
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1', 'password2']

class AvailabilityForm(forms.Form):
    ROOM_CATEGORIES = [
        ('YAC','AC'),
        ('NAC','NON-AC'),
        ('DEL','DELUXE'),
        ('KIN','KING'),
        ('QUE','QUEEN'),
    ]
    room_category = forms.ChoiceField(choices=ROOM_CATEGORIES,required=True)
    check_in = forms.DateTimeField(required=True)


