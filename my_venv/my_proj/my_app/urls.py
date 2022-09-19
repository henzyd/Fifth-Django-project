from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page_func),
    path('second/', views.second_page_func),
]
