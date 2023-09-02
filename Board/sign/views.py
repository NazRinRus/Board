from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .models import BaseRegisterForm
from django.views import View

class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = 'sign/endsignup/'


