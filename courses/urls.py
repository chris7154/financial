from django.urls import path
from . import views


urlpatterns = [
    path('', views.course_list, name='course_list'),               # List of courses
    path('create/', views.course_create, name='course_create'),     # Create a new course
    path('detail/<int:pK>/', views.course_details, name='course_details'),  # Course detail page
]