from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from .models import Message
from django.contrib.auth.models import User

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('chat:chat')
    else:
        form = SignUpForm()
    return render(request, 'chat/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('chat:chat')
    else:
        form = AuthenticationForm()
    return render(request, 'chat/login.html', {'form': form})

def chat(request):
    users = User.objects.exclude(username=request.user.username)
    messages = Message.objects.filter(recipient=request.user)
    return render(request, 'chat/chat.html', {'users': users, 'messages': messages})
