from django.urls import path

from . import views

app_name = 'book_borrow'

urlpatterns = [
    path('borrow', views.book_borrow, name='borrow'),
    path('give-back', views.book_give_back, name='give-back'),
]
