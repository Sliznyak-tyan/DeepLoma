from django.shortcuts import render
from django.shortcuts import redirect

from control_center.endpoints import heat_handler
from control_center.constans import LOGIN_REDIRECTION_URL
from control_center.constans import STATISTICS_HTML_PATH


def statistics_view(request):
    if not request.user.is_authenticated:
        return redirect(LOGIN_REDIRECTION_URL)
    heat_data = heat_handler()
    return render(request, STATISTICS_HTML_PATH, {'data': heat_data})
