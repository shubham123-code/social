from ast import Pass
from cmath import inf
import email
import re
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from core.models import Profile
# Create your views here.
def index(request):
    return render(request, 'index.html')
def signup(request):
    
    if request.method == 'POST' :
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1'] 
        password2 = request.POST['password2']
        if(password1==password2):
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exits')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email,password=password1)
                user.save()
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('signup')
        else:
            messages.info(request, 'Password does not match.')
            return redirect('signup')
    else:
        return render(request, 'signup.html')

def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            messages.info(request, 'You are successfully logged in!')
            return redirect('signin')
        else:
            messages.info(request, 'Username or password incorrect')
            return redirect('signin')
    else:
        return render(request, 'signin.html')
    
    