from django.shortcuts import render
import requests
from django.contrib.auth.models import User
import json


# Create your views here.

# handles viewing and editing of profile data
def details(request):
    editable_fields = ['name', 'email', 'blog', 'twitter_username', 'company', 'location', 'hireable', 'bio']

    # if the profile has been updated, then PATCH github profile with new profile information
    if request.method == "GET":
        body = {}
        for key in request.GET:
            if key in editable_fields and request.GET[key] is not "":
                body[key] = request.GET[key]

        user = User.objects.get(username=request.user.username)
        social = user.social_auth.get(provider='github')
        response = requests.patch(
            'https://api.github.com/user',
            headers={
                'Authorization': 'token ' + social.extra_data['access_token'],
                'Content-Type': 'application/json',
                'Accept': 'application/vnd.github.v3+json'
            },
            data=json.dumps(body)
        )
        data = response.json()

    # if the profile has NOT been updated, simply GET the profile info and render
    else:
        user = User.objects.get(username=request.user.username)
        social = user.social_auth.get(provider='github')
        response = requests.get(
            f'https://api.github.com/users/{request.user.username}',
            headers={'Authorization': 'token ' + social.extra_data['access_token']}
        )
        data = response.json()

    # not all profile data is editable, splits dict into editable and non-editable
    editable_data = dict((d, data.pop(d)) for d in editable_fields)

    return render(request, 'details.html', {'editable_data': editable_data, 'non_editable_data': data})
