from django.urls import path
from .views import IndicatorsView
from .views import StatisticsView
from .views import ScheduleView

urlpatterns = [path('indicators/', IndicatorsView.as_view()),
               path('statistics/', StatisticsView.as_view()),
               path('schedule/', ScheduleView.as_view())]
