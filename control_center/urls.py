from django.urls import path
from .views import indicators_view
from .views import statistics_view
from .views import schedule_view
from .views import login_view
from .views import logout_view

urlpatterns = [path('indicators/', indicators_view),
               path('statistics/', statistics_view),
               path('schedule/', schedule_view),
               path('login/', login_view),
               path('logout/', logout_view)]
