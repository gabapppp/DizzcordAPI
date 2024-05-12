from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_notfication_list, name='list')
]