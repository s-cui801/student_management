from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from students.models import Student
from students.forms import StudentForm, StudentSearchForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
# Path: students/views.py
'''Display a list of all students'''
def students_list(request):
    form = StudentSearchForm(request.GET)
    students = Student.objects.all().order_by('-enrollment_date')
    
    if form.is_valid():
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        # Filter students by first name if it was submitted
        if first_name:
            students = students.filter(first_name__icontains=first_name)
        # Filter students by last name if it was submitted
        if last_name:
            students = students.filter(last_name__icontains=last_name)

    # Implement pagination (5 students per page)
    paginator = Paginator(students, 5)  # Show 5 students per page
    page_number = request.GET.get('page')  # Get the current page number
    try:
        page_obj = paginator.get_page(page_number)
    except (ValueError, TypeError):
        page_obj = paginator.get_page(1)  # Default to the first page if the input is invalid
    # page_obj = paginator.get_page(page_number)  # Get the students for the current page

    context = {
        'students': students,
        'form': form,
        'page_obj': page_obj,
    }
    return render(request, 'students/list.html', context)

'''Display the details of a single student'''
def students_detail(request, student_id):
    # student = Student.objects.get(id=student_id)
    # student = get_object_or_404(Student, pk=pk)  # If student doesn't exist, a 404 error will be raised
    # Manually handle the 404 error
    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        raise Http404("Student does not exist.")
    context = {
        'student': student,
    }
    return render(request, 'students/detail.html', context)

'''Add a new student'''
@login_required
def students_add(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = Student(
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                date_of_birth=form.cleaned_data['date_of_birth'],
                enrollment_date=form.cleaned_data['enrollment_date'],
                grade=form.cleaned_data['grade'],
            )
            student.save()
            return HttpResponseRedirect('/students/')
        else:
            context = {
                'form': form,
            }
            return render(request, 'students/add.html', context)
    else: context = {
        'form': StudentForm(),
        }
    return render(request, 'students/add.html', context)

'''Edit an existing student'''
@login_required
def students_edit(request, student_id):
    # student = Student.objects.get(id=student_id)
    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        raise Http404("Student does not exist.")
    
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student.first_name = form.cleaned_data['first_name']
            student.last_name = form.cleaned_data['last_name']
            student.email = form.cleaned_data['email']
            student.date_of_birth = form.cleaned_data['date_of_birth']
            student.enrollment_date = form.cleaned_data['enrollment_date']
            student.grade = form.cleaned_data['grade']
            student.save()
            return HttpResponseRedirect('/students/')
        else:
            print("Form is invalid. Errors:", form.errors)  # Debug statement
    else: 
        form = StudentForm(initial={
            'first_name': student.first_name,
            'last_name': student.last_name,
            'email': student.email,
            'date_of_birth': student.date_of_birth,
            'enrollment_date': student.enrollment_date,
            'grade': student.grade,
        })
    context = {
        'form': form,
        'student': student,
    }
    return render(request, 'students/edit.html', context)

'''Delete an existing student'''
@login_required
def students_delete(request, student_id):
    student = Student.objects.get(id=student_id)
    student.delete()
    return HttpResponseRedirect('/students/')
