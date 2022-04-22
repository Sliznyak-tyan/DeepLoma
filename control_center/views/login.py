from django.shortcuts import render
from control_center.endpoints import login_handler
from control_center.constans import LOGIN_HTML_PATH


def login_view(request):
    if request.method == 'POST':
        return login_handler(request)
    else:
        return render(request, LOGIN_HTML_PATH)
