import csv
import io
from rest_framework import views, generics, status
from rest_framework.response import Response
from django.db.models import Avg
from .models import Student, Subject, Test, Result
from .serializers import (
    StudentSerializer,
    SubjectSerializer,
    TestSerializer,
    ResultSerializer,
    StudentPerformanceSerializer,
    SubjectAnalyticsSerializer,
    LeaderboardSerializer
)

class UploadResultsView(views.APIView):
    def post(self, request):
        file = request.FILES.get('file')
        if not file:
            return Response({"error": "No file uploaded"}, status=400)

        decoded_file = file.read().decode('utf-8')
        reader = csv.DictReader(io.StringIO(decoded_file))
        results_to_create = []

        for row in reader:
            try:
                student_id = int(row['sturecid'])
                test_id = int(row['testid'])
                total_marks = sum(
                    int(row.get(f'a{i}', 0)) if row.get(f'a{i}', 0).isdigit() else 0
                    for i in range(1, 181)
                )

                student = Student.objects.get(id=student_id)
                test = Test.objects.get(id=test_id)

                result = Result(
                    student=student,
                    test=test,
                    marks_scored=total_marks
                )
                results_to_create.append(result)

            except Exception as e:
                print(f"Error processing row: {e}")

        Result.objects.bulk_create(results_to_create)

        return Response({
            "status": "Data uploaded successfully",
            "records_created": len(results_to_create)
        })

class StudentPerformanceView(views.APIView):
    def get(self, request, student_id):
        try:
            student = Student.objects.get(id=student_id)
            results = Result.objects.filter(student=student)
            data = {
                "student": student.name,
                "tests": [
                    {
                        "test_id": r.test.id,
                        "subject": r.test.subject.name,
                        "test_type": r.test.test_type,
                        "marks_scored": r.marks_scored,
                        "total_marks": r.test.total_marks
                    }
                    for r in results
                ]
            }
            return Response(data)
        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=404)

class SubjectAnalyticsView(views.APIView):
    def get(self, request, subject_id):
        try:
            subject = Subject.objects.get(id=subject_id)
            tests = Test.objects.filter(subject=subject)
            results = Result.objects.filter(test__in=tests)
            avg_score = results.aggregate(Avg('marks_scored'))['marks_scored__avg'] or 0
            data = {
                "subject": subject.name,
                "average_score": round(avg_score, 2)
            }
            return Response(data)
        except Subject.DoesNotExist:
            return Response({"error": "Subject not found"}, status=404)

class LeaderboardView(views.APIView):
    def get(self, request, test_id):
        try:
            test = Test.objects.get(id=test_id)
            results = Result.objects.filter(test=test).order_by('-marks_scored')
            data = [
                {
                    "student": r.student.name,
                    "marks_scored": r.marks_scored
                }
                for r in results
            ]
            return Response(data)
        except Test.DoesNotExist:
            return Response({"error": "Test not found"}, status=404)
