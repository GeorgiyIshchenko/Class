from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from django.contrib import auth
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.utils import timezone, dateformat

from .forms import *
from .models import *

def homepage(request):
	return render(request,'homepage.html')

def sign_up(request):
	if request.method == 'POST':
		user_form = UserForm(request.POST)
		profile_form = ProfileForm(request.POST)
		password_form = PasswordForm(request.POST)
		if user_form.is_valid() and profile_form.is_valid() and password_form.is_valid():
			user = user_form.save(commit=False)
			profile_user = User.objects.create_user(username = user.email,
				email=user.email,
				first_name=user.first_name,
				last_name=user.last_name,
				password=password_form.cleaned_data.get("password"),
				)
			profile_user.save()
			profile = profile_form.save(commit=False)
			profile.user = profile_user
			profile.save()
			return redirect('/')
	else:
		user_form = UserForm()
		password_form = PasswordForm()
		profile_form = ProfileForm()
	return render(request,'sign_up.html',{
		'user_form' : user_form,
		'password_form' : password_form,
		'profile_form' : profile_form
		})

def sign_in(request):
	if request.method=="POST":
		sign_in_form = SignInForm(request.POST)
		if sign_in_form.is_valid():
			email = sign_in_form.cleaned_data.get('email')
			password = sign_in_form.cleaned_data.get('password')
			user = auth.authenticate(username = email, password=password)
			if user is not None and user.is_active:
				auth.login(request, user)
				return redirect('/')
	else:
		sign_in_form = SignInForm()
	return render(request,'sign_in.html',{
		'sign_in_form':sign_in_form,
		})

def profile(request,pk):
	profile = Profile.objects.get(pk=pk)
	return render(request, 'profile.html', {
		'profile' : profile
		})
