from django.urls import path

import author.views

app_name = 'author'

urlpatterns = [
    path('', author.views.author_list, name='list'),
    path('<int:author_id>', author.views.author_detail, name='detail'),
]
