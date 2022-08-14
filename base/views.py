from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .mlmodel import ranker
import json

# Create your views here.

def signin(request):
    context = {}

    if request.user.is_authenticated:
        return redirect('ranker')


    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User doesnt exist')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('ranker')
        else:
            messages.error(request, 'Incorrect Password')

    return render(request, 'base/signin.html', context)

def logout_user(request):
    logout(request)
    return redirect('signin')

@login_required(login_url='signin')
def machine(request):
    user = request.user
    solved = False
    result = " "
    slice_size = 5
    if request.method == "POST":
        try:
            text = request.POST.get("large_text")
            slice_size = int(request.POST.get('slice_size'))
            # result = ranker(text, sent_lim=slice_size)

            content_first = {
                "text": text,
                "sentence_limit": slice_size
            }
            content = json.dumps(content_first)
            data = content

            json_result = ranker(context=data)

            slice_size = str(json_result["sentence_limit"])
            result = str(json_result["result"])
            solved = True
        except:
            solved = False
    
    context = {
        'slice_size': slice_size,
        'result': result,
        'solved': solved,
        'user': user,
        }
    return render(request, 'base/main.html', context)




