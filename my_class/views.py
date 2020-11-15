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
			profile_user = User.objects.create_user(username = user_form.cleaned_data['email'],
				email=user_form.cleaned_data['email'],
				first_name=user_form.cleaned_data['first_name'],
				last_name=user_form.cleaned_data['last_name'],
				)
			profile_user.set_password(password_form.cleaned_data.get("password"))
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

def profile(request):
	profile = Profile.objects.get(user = request.user)
	print(profile.classes)
	return render(request, 'profile.html', {
		'profile' : profile
		})

def edit_profile(request):
	if request.method == 'POST':
		user_form = UserForm(request.POST, instance=request.user)
		profile_form = ProfileForm(request.POST, instance=request.user.profile)
		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			return redirect('/im')
	else:
		user_form = UserForm(instance=request.user)
		profile_form = ProfileForm(instance=request.user.profile)
	return render(request,'profile_edit.html',{
		'user_form' : user_form,
		'profile_form' : profile_form
		})


def logout(request):
	auth.logout(request)
	return redirect("/sign_in")


def class_view(request,name,pk):
	pass


def class_join(request):
	if request.method=="POST":
		pass
	else:
		class_join_form = ClassJoin()
	return render(request,'class_join.html',{
		'class_join_form':class_join_form,
		})


def class_create(request):
	if request.method=="POST":
		class_create_form = ClassCreate(request.POST)
		if class_create_form.is_valid():
			current_class = class_create_form.save(commit=False)
			current_class.teacher = request.user.profile 
			current_class.save()
			request.user.profile.classes.add(current_class)
			return redirect('/im')
	else:
		class_create_form = ClassCreate()
	return render(request,'class_create.html',{
		'class_create_form':class_create_form,
		})


def class_leave(request):
	pass

