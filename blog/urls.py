from django.urls import path
from . import views

from .views import (
        PostListVeiw, 
        PostDetailVeiw, 
        PostCreateVeiw,
        PostUpdateVeiw,
        PostDeleteVeiw,
        UserPostListVeiw
)
urlpatterns = [
    path('', PostListVeiw.as_view(), name="blog-home"),
    path('user/<str:username>', UserPostListVeiw.as_view(), name="user-posts"),
    path('post/<int:pk>/', PostDetailVeiw.as_view(), name="post-detail"),
    path('post/new/', PostCreateVeiw.as_view(), name="post-create"),
    path('post/<int:pk>/update/', PostUpdateVeiw.as_view(), name="post-update"),
    path('post/<int:pk>/delete/', PostDeleteVeiw.as_view(), name="post-delete"),
    path("about/", views.about, name="blog-about"),
    path("test/", views.test, name="test")
]
