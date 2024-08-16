from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signup),
    path("userlist", views.userlist),
    path("update_user/<int:pk>/", views.update_user),
    path("login", views.loginUser),
    path("logout", views.logoutUser),
    # blog urls
    path('blogs/', views.list_blogs, name='blog-list'),
    path('create/', views.create_blog, name='blog-create'),
    path('retrieve/<int:pk>/', views.retrieve_blog, name='blog-retrieve'),
    path('update/<int:pk>/', views.update_blog, name='blog-update'),
    path('delete/<int:pk>/', views.delete_blog, name='blog-delete'),
    path('search/', views.search, name='search'),

]
