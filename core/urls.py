from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_page, name='upload_page'),
    path('upload/', views.upload_csv, name='upload_csv'),
    path('student/<int:student_id>/', views.student_performance, name='student_performance'),
    path('leaderboard/<int:test_id>/', views.leaderboard, name='leaderboard'),
    path('subject/<int:subject_id>/', views.subject_analytics, name='subject_analytics'),
]
