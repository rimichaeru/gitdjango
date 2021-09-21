from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .form import LoginForm
from django.http import HttpResponse
import requests
from django.contrib.auth.models import User
import json


# Create your views here.

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            clean_data = form.cleaned_data
            user = authenticate(request, username=clean_data['username'], password=clean_data['password'])

            if user is not None:
                login(request, user)
                return HttpResponse('Authentication successful')
            else:
                return HttpResponse('Authentication failed')

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def details(request):
    user = User.objects.get(username=request.user.username)
    social = user.social_auth.get(provider='github')
    response = requests.get(
        f'https://api.github.com/users/{request.user.username}',
        headers={'Authorization': 'token ' + social.extra_data['access_token']}
    )
    data = response.json()

    return render(request, 'details.html', {'data': data.values, 'token': social.extra_data['access_token']})


def update_user(request):
    user = User.objects.get(username=request.user.username)
    social = user.social_auth.get(provider='github')
    response = requests.patch(
        'https://api.github.com/user',
        headers={
            'Authorization': 'token ' + social.extra_data['access_token'],
            'Content-Type': 'application/json',
            'Accept': 'application/vnd.github.v3+json'
        },
        data=json.dumps({"company": "N/A"})
    )
    data = response.json()

    return render(request, 'update.html', {'data': data.values})
