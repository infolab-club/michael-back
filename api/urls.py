from django.urls import path
from django.contrib import admin

from . import views

app_name = 'api'
urlpatterns = [
    path('get/', views.IncidentView.as_view()),
    path('cats/', views.CategoryView.as_view())
]