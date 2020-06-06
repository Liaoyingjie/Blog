from django.urls import path
from . import views

urlpatterns = [
    path('<int:article_id>', views.article_detail, name='article_detail_url'),
    path('', views.article_list, name='article_list_url')
]