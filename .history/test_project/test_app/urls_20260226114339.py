from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/test_project/MyView', views.MyView, name='MyView')
]