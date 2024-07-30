from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-author/', views.add_author, name='add_author'),
    path('add-book/', views.add_book, name='add_book'),
    path('add-publisher/', views.add_publisher, name='add_publisher'),
    path('search/', views.search, name='search'),
]
