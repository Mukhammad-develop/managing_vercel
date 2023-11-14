from django import forms
from django.contrib.auth.models import User
from . import models


class StudentUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']


class StudentExtraForm(forms.ModelForm):
    class Meta:
        model = models.StudentExtra
        fields = ['cl', 'mobile', 'status']


class AdminSigupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']


class TeacherUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']


class TeacherExtraForm(forms.ModelForm):
    class Meta:
        model = models.TeacherExtra
        fields = ['mobile', 'status']


class NoticeForm(forms.ModelForm):
    class Meta:
        model = models.Notice
        fields = '__all__'
