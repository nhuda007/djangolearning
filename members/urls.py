
from django.urls import path
from . import views
urlpatterns = [
    path('', views.members, name='members'),
    path('form/', views.add_member, name='form'),
]
