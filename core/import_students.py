import csv
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_analytics.settings')
django.setup()

from core.models import Student

csv_path = 'STUDENTS RESPONSE 1.csv'

with open(csv_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    count = 0
    for row in reader:
        student_id = int(row['sturecid'])
        name = row['sname']
        email = f"{name.lower().replace(' ', '')}@example.com"
        roll_number = f"ROLL{student_id}"

        student, created = Student.objects.get_or_create(
            id=student_id,
            defaults={'name': name, 'email': email, 'roll_number': roll_number}
        )
        if created:
            count += 1
            print(f"Inserted student {student_id} - {name}")
        else:
            print(f"Student {student_id} already exists")

    print(f"\nTotal students inserted: {count}")
