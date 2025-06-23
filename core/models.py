from django.db import models

class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    roll_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Test(models.Model):
    id = models.IntegerField(primary_key=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    test_type = models.CharField(max_length=50)
    date = models.DateField()
    total_marks = models.IntegerField()

    def __str__(self):
        return f"{self.subject.name} - {self.test_type}"

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    marks_scored = models.IntegerField()

    class Meta:
        unique_together = ('student', 'test')
