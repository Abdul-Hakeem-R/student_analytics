from django.urls import path
from .views import (
    UploadResultsView,
    StudentPerformanceView,
    SubjectAnalyticsView,
    LeaderboardView
)

urlpatterns = [
    path('upload/', UploadResultsView.as_view(), name='upload-results'),
    path('students/<int:student_id>/performance/', StudentPerformanceView.as_view(), name='student-performance'),
    path('subjects/<int:subject_id>/analytics/', SubjectAnalyticsView.as_view(), name='subject-analytics'),
    path('tests/<int:test_id>/leaderboard/', LeaderboardView.as_view(), name='test-leaderboard'),
]
