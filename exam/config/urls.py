from django.contrib import admin
from django.urls import path, include

from .views import index as index_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('common/', include('common.urls')),
    path('authors/', include('author.urls')),
    path('books/', include('book.urls')),
    path('books/<int:book_id>/book-borrow/', include('book_borrow.urls')),
]
