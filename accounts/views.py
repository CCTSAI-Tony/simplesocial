from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms

# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login") # don't want this to execute until they've hit submit instead of normal reverse
    template_name = "accounts/signup.html"

# Create your views here.
