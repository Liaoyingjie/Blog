from django.urls import path
from . import views

urlpatterns = [
    #http:xx.xx.xx.xx/blog/
    path('<int:blog_id>',views.blog_detail,name='blog_detail_url'),
    path('type/<int:blog_type_pk>',views.blogs_with_type, name='blogs_with_type_url'),

]