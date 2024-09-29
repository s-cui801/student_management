from django.shortcuts import render
from students.models import Student

# Create your views here.
# Path: students/views.py
'''Display a list of all students'''
def students_list(request):
    students = Student.objects.all().order_by('-enrollment_date')
    context = {
        'students': students,
    }
    return render(request, 'students/list.html', context)

'''Display the details of a single student'''
def students_detail(request, student_id):
    student = Student.objects.get(id=student_id)
    context = {
        'student': student,
    }
    return render(request, 'students/detail.html', context)

'''Add a new student'''
def students_add(request):
    return render(request, 'students/add.html')

'''Edit an existing student'''
def students_edit(request, student_id):
    student = Student.objects.get(id=student_id)
    context = {
        'student': student,
    }
    return render(request, 'students/edit.html', context)