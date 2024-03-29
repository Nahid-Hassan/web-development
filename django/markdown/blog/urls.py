from django.urls import path

from .views import BlogListView
from . import views

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('post/<int:pk>', views.home, name='home'),
]
