from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('python/tutorial', views.tutorial, name='tutorial'),
]
