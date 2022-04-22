from django.shortcuts import render
from django.shortcuts import redirect

from control_center.constans import LOGIN_REDIRECTION_URL
from control_center.constans import SCHEDULE_HTML_PATH
from control_center.endpoints import schedule_handler
from control_center.endpoints import recuperator_get_schedule_handler


def schedule_view(request):
    if not request.user.is_authenticated:
        return redirect(LOGIN_REDIRECTION_URL)
    if request.method == 'POST':
        return schedule_handler(request)
    else:
        schedule = recuperator_get_schedule_handler()
        return render(request, SCHEDULE_HTML_PATH, {'schedule': schedule})
