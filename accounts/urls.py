from django.urls import path
from . import views

urlpatterns = [
    # URL pattern for listing all users
    path('users/', views.user_list, name='user_list'),

    # URL pattern for viewing a specific user
    path('users/<int:user_id>/', views.user_detail, name='user_detail'),

    # URL pattern for creating a new user (new)
    path('create/', views.create_user, name='create_user'),
]