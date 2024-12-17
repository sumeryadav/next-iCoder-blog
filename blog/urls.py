from django.contrib import admin
from django.urls import path
from .import views
from .views import like_post

urlpatterns = [
    # API to post a comment
    path('post/comment/', views.postComment, name='postComment'),
    path('', views.blogHome, name='blogHome'),
    path('<str:slug>', views.blogPost, name='blogPost'),
    path('like/<int:pk>/', like_post, name='like_post'),
]
