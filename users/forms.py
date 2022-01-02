from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms.models import ModelForm

from users.models import Questions


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name', 'password1', 'password2']


class Questionform(ModelForm):
    questions_id = forms.IntegerField()
    question =  forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":20}))

    class Meta:
        model = Questions
        fields = ['questions_id','question']