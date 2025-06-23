import csv
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_analytics.settings')
django.setup()

from core.models import Subject, Test

csv_path = 'STUDENTS RESPONSE 1.csv'  


subject_name = 'CUMULATIVE TEST'
subject, _ = Subject.objects.get_or_create(name=subject_name)

test_ids = set()

with open(csv_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        test_id = int(row['testid'])
        test_ids.add(test_id)

for test_id in test_ids:
    test, created = Test.objects.get_or_create(
        id=test_id,
        defaults={
            'subject': subject,
            'test_type': 'Monthly',
            'date': '2025-06-16',
            'total_marks': 720  # 180 * 4 
        }
    )
    if created:
        print(f"Inserted test {test_id}") # checks duplicates
    else:
        print(f"Test {test_id} already exists")
