from django.urls import path
from .views import IndicatorsView
from .views import StatisticsView
from .views import schedule_view

urlpatterns = [path('indicators/', IndicatorsView.as_view()),
               path('statistics/', StatisticsView.as_view()),
               path('schedule/', schedule_view)]
