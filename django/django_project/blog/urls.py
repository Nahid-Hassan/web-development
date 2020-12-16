from django.urls import path
from . import views


urlpatterns = [
    # path(route, view, kwargs=None, name=None)
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
