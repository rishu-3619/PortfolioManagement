"""Defines URL patterns for Portfolio Manager."""

from django.urls import path
#this is the path function needed when mapping URLs to views

from . import views

app_name = 'PortfolioManagerHome'
urlpatterns = [
    #Home Page
    path('', views.index, name='index'),

    #About Page
    path('about/', views.about, name='about'),
]

