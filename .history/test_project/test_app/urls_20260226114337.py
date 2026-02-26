from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/test_project/healthcheck', views.MyView, name='MyView')
]