from django.shortcuts import render
from django.shortcuts import redirect

from control_center.endpoints import get_indicators_data
from control_center.constans import LOGIN_REDIRECTION_URL
from control_center.constans import INDICATORS_HTML_PATH


def indicators_view(request):
    if not request.user.is_authenticated:
        return redirect(LOGIN_REDIRECTION_URL)
    data = get_indicators_data()
    return render(request, INDICATORS_HTML_PATH, {'data': data})
