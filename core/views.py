from django.shortcuts import render, redirect,get_object_or_404
from django.db.models import Sum
from django.contrib import messages
from .models import Student, Subject, Test, Result

def upload_page(request):
    return render(request, 'core/upload.html')

def upload_csv(request):
        return render(request, 'core/upload.html')

def student_performance(request, student_id):
    student = Student.objects.get(id=student_id)
    results = Result.objects.filter(student=student)
    return render(request, 'core/student_performance.html', {'student': student, 'results': results})

def leaderboard(request, test_id):
    test = Test.objects.get(id=test_id)
    results = Result.objects.filter(test=test).order_by('-marks_scored')
    return render(request, 'core/leaderboard.html', {'test': test, 'results': results})

def subject_analytics(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    tests = Test.objects.filter(subject=subject)

    total_marks = 0
    total_students = 0

    for test in tests:
        test_total = Result.objects.filter(test=test).aggregate(total=Sum('marks_scored'))['total'] or 0
        student_count = Result.objects.filter(test=test).count()

        total_marks += test_total
        total_students += student_count

    average = total_marks / total_students if total_students else 0

    return render(request, 'core/subject_analytics.html', {
        'subject': subject,
        'average': average
    })
