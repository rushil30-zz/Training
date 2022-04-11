#-*- coding: utf-8 -*-
from django import forms
from django.core.validators import FileExtensionValidator

class LoginForm(forms.Form):
    user = forms.CharField(max_length=15)
    password = forms.CharField(widget = forms.PasswordInput())

class ProfileForm(forms.Form):
    name = forms.CharField(max_length=100)
    picture = forms.ImageField()
    
class SendMailForm(forms.Form):
    email_id = forms.EmailField()
    email_cc = forms.EmailField()
    email_bcc = forms.EmailField()
    subject = forms.CharField(max_length=200)
    msg = forms.CharField(widget=forms.Textarea)
    attachment = forms.FileField(validators=[FileExtensionValidator(allowed_extensions=['png', 'txt', 'jpg'])])
