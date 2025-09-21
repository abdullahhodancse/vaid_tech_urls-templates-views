from django.db import migrations

def migrate_department(apps, schema_editor):
    Student = apps.get_model('app1', 'Student')
    Department = apps.get_model('app1', 'Department')

    for student in Student.objects.all():
        if student.department:
            dept_obj = Department.objects.filter(name=student.department).first()
            if not dept_obj: 
                dept_obj = Department.objects.create(name=student.department)
            student.new_department = dept_obj
            student.save()

class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_alter_student_department'),
    ]

    operations = [
        migrations.RunPython(migrate_department),
    ]
