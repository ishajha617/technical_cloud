from django.urls import path
from . import views

urlpatterns = [

    # Home Page
    path('', views.home, name='home'),

    # Course List Page
    path('courses/', views.course_list, name='course_list'),

    # Course Detail Page
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),

    # Enrollment Page
    path('enroll/<int:course_id>/', views.enroll, name='enroll'),
]