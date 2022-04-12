from django.urls import path
from .views import IndicatorsView
from .views import StatisticsView

urlpatterns = [path('indicators/', IndicatorsView.as_view()),
               path('statistics/', StatisticsView.as_view())]
