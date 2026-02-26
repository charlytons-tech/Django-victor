from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ahealthcheck/', views.healthcheck, name='healthCheck')
]