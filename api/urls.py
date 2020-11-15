from django.urls import path
from django.contrib import admin

from . import views

app_name = 'api'
urlpatterns = [
    path('get/', views.MessageView.as_view()),
    path('cats/', views.CategoryView.as_view()),
    path('areas/', views.AreaView.as_view()),
    path('regmess/', views.MessageRegisterView.as_view()),
    path('getlasts/', views.AccidentView.as_view())
]