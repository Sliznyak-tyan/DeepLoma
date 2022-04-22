from django.shortcuts import redirect
from django.contrib.auth import logout
from control_center.constans import LOGIN_REDIRECTION_URL


def logout_view(request):
    logout(request)
    return redirect(LOGIN_REDIRECTION_URL)
