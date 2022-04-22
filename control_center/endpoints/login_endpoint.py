from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from control_center.constans import INDICATORS_REDIRECTION_URL


def login_handler(request):
    username = request.POST['login']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(INDICATORS_REDIRECTION_URL)
