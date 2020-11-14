from django.urls import path
from django.contrib import admin

from . import views

app_name = 'api'
urlpatterns = [
    path('', views.IncidentView.as_view()),
]