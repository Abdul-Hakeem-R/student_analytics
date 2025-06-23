from rest_framework import serializers
from .models import Student, Subject, Test, Result

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'

class StudentPerformanceSerializer(serializers.Serializer):
    student = serializers.CharField()
    tests = serializers.ListField()

class SubjectAnalyticsSerializer(serializers.Serializer):
    subject = serializers.CharField()
    average_score = serializers.FloatField()

class LeaderboardSerializer(serializers.Serializer):
    student = serializers.CharField()
    marks_scored = serializers.IntegerField()
