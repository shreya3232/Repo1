from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import Questionform, UserRegisterForm
from django.contrib.auth import login,authenticate


def register(response):
    if response.method == 'POST':
        form = UserRegisterForm(response.POST)
        if form.is_valid:
           form.save()
           return redirect('/home')
    else:
        form =  UserRegisterForm()

    return render(response,'register.html',{'registerform':form})

def home(response):

    return render(response,'home.html',{})

def registerquestion(response):
    if response.method=='POST':
        form=Questionform(response.POST)
        if form.is_valid:
           form.save()
           return redirect('/home')
    else:
         form =  Questionform()
        # return redirect("/home")

    return render(response,'questions.html',{'questionform':form})      