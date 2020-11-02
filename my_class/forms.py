from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from django import forms
from .models import *

class UserForm(forms.ModelForm):
	first_name = forms.CharField(label='Введите имя', widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
	last_name = forms.CharField(label='Введите фамилию',widget=forms.TextInput(attrs={'placeholder': 'Фамилия'}))
	email = forms.CharField(label='Введите e-mail',widget=forms.TextInput(attrs={'placeholder': 'E-mail'}))

	class Meta:
		model = User
		fields = ('first_name','last_name','email',)

class ProfileForm(forms.ModelForm):
	institution = forms.CharField(label='Укажите свое учебное заведение', 
		widget=forms.TextInput(attrs={'placeholder': 'Учебное заведение'}))
	grade = forms.CharField(label='Укажите свой класс (курс)', 
		widget=forms.TextInput(attrs={'placeholder': 'Класс (курс)'}))

	class Meta:
		model = Profile
		fields = ('institution','grade',)

class PasswordForm(forms.Form):
	password = forms.CharField(label='Придумайте пароль', 
		widget=forms.PasswordInput())

class SignInForm(forms.Form):
	email = forms.CharField(label='Введите e-mail', widget=forms.TextInput(attrs={'placeholder': 'E-mail'}))
	password = forms.CharField(label='Введите пароль', 
		widget=forms.PasswordInput())