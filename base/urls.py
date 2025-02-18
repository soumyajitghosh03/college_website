from django.contrib import admin
from django.urls import path
from base import views

urlpatterns = [
    path('', views.home),
    path('about', views.about),
    path('academics', views.academics),
    path('campus', views.campus),
    path('hostel', views.hostel),
    path('admission', views.admission),
    path('faculty', views.faculty),
    path('demo', views.contact),
    path('feedback', views.feedback),
]