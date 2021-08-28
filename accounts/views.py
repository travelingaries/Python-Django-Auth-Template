import json

from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserProfile


def signup(request):
    if request.method == "POST":
        form_data = dict()
        for field in json.loads((request.POST)['form_data']):
            form_data[field['name']] = field['value']
        if User.objects.filter(email=form_data['email']).exists():
            response = JsonResponse({"error": "same email already exists"})
            response.status_code = 401
            return response
        if User.objects.filter(username=form_data['username']).exists():
            response = JsonResponse({"error": "same nickname already exists"})
            response.status_code = 401
            return response
        if UserProfile.objects.filter(phone=form_data['phone']).exists():
            response = JsonResponse({"error": "same phone number already exists"})
            response.status_code = 401
            return response
        user = User.objects.create_user(
            username=form_data['username'],
            password=form_data['password'],
            email=form_data['email'],
            first_name=form_data['first_name'],
        )
        user_profile = UserProfile.objects.create(
            phone=form_data['phone']
        )
        user_profile.user = user
        user_profile.save()

        response = JsonResponse({})
        response.status_code = 200
        return response
    else:
        return render(request, 'registration/signup.html')


def custom_login(request):
    if request.method == "POST":
        form_data = dict()
        for field in json.loads((request.POST)['form_data']):
            form_data[field['name']] = field['value']

        username = ''
        if form_data['login_option'] == 'email':
            user = User.objects.filter(email=form_data['login_option_value'])
            if user.exists():
                username = user[0]
        elif form_data['login_option'] == 'name':
            if form_data['email'] == '':
                user = User.objects.filter(first_name=form_data['login_option_value'])
            else:
                user = User.objects.filter(first_name=form_data['login_option_value'], email=form_data['email'])
            if user.exists():
                if user.count() > 1:
                    response = JsonResponse({"error": "need additional info"})
                    response.status_code = 401
                    return response
                username = user[0]
        elif form_data['login_option'] == 'nickname':
            username = form_data['login_option_value']
        elif form_data['login_option'] == 'phone':
            user_profile = UserProfile.objects.filter(phone=form_data['login_option_value'])
            if user_profile.exists():
                username = user_profile[0]
        if username == '':
            response = JsonResponse({"error": "no registered user"})
            response.status_code = 400
            return response

        user = authenticate(username=username, password=form_data['password'])
        if user is None:
            response = JsonResponse({"error": "no registered user"})
            response.status_code = 400
            return response
        else:
            login(request, user)
            response = JsonResponse({})
            response.status_code = 200
            return response
    else:
        return render(request, 'registration/login.html')


def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html', {
            'email': request.user.email,
            'name': request.user.first_name,
            'nickname': request.user.username,
            'phone': '01030974325',
        })
    else:
        return redirect('/accounts/login/')


def reset_password(request):
    if request.method == "POST":
        form_data = dict()
        for field in json.loads((request.POST)['form_data']):
            form_data[field['name']] = field['value']
        user = User.objects.get(username=form_data['username'])
        user.set_password(form_data['password'])
        user.save()

        response = JsonResponse({})
        response.status_code = 200
        return response
    else:
        return render(request, 'registration/reset_password.html')


def check_phone(request):
    if request.method == "POST":
        form_data = dict()
        for field in json.loads((request.POST)['form_data']):
            form_data[field['name']] = field['value']
        user_profile = UserProfile.objects.filter(phone=form_data['phone'])
        if user_profile.exists():
            response = JsonResponse({"username": user_profile[0].user.username})
            response.status_code = 200
            return response
        else:
            response = JsonResponse({"error": "no registered user"})
            response.status_code = 400
            return response
    else:
        return redirect('/accounts/profile')
