# Student Management System Report
## 1. Project Setup
### Set up the development environment
// TODO:
### Start the Django project
In the console, use the following command to start the Django project.
```
django-admin startproject student_management .
```
Note: If there is no dot at the end, Django will create a nested project directory, e.g. `/student_management/student_management`.
Use the following command to run the project.
```
py manage.py runserver
```
The project runs successfully.
![alt text](images/image.png)

### Add the students app

## 2. Create Student Model
### Describe the database schema in models.py
### Create a migration
### Apply the migrations and create databases

## 3. Set up admin interface
### Apply existing migrations
```shell
(venv) D:\24fall-term\GNG5300\Django-projects\student_management>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, students
Running migrations:
  ...
```
### Add a superuser
```
python manage.py createsuperuser
```
Navigate to `http://localhost:8000/admin/` and log in with the credentials to see the following page:

![alt admin page](images/image-1.png)

### Register the Student model and customize the list display
In the students folder, find admin.py and register the model using the following code:
```python
from django.contrib import admin
from .models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'enrollment_date')
    ordering = ('-enrollment_date',)

admin.site.register(Student, StudentAdmin)
```
Now the Student model is visible in the admin page, and it only displays the first name, last name, and enrollment date.
![alt text](images/image-2.png)

## 4. Views and Templates
I created four view functions for my students app in the `views.py` file in the `students/` directory:
- **students_list( )** will display a list of all students.
- **students_detail( )** will display the detail of one student. 
- **students_add( )** will later show a form to allow users to add a new student.
- **students_edit( )** will later show a form to allow users to update information of an existing student.

```python
# students/views.py
from django.shortcuts import render
from students.models import Student

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
```
After adding corresponding templates for each view, this is what each web page looks like:
### Display a list of all students
![alt text](images/image-5.png)
Url:  `http://localhost:8000/students/`
It displays a list of all students, with detail and edit button at the end of each row. It also has a button for adding a new student at the end of the list.
### Display the details of a single student
![alt text](images/image-4.png)
Url: `http://localhost:8000/students/detail/1/`
It shows details of a single student and has a button for editing the student's information.
### Add a new student
![alt text](images/image-6.png)
It is an empty page for now.
### Edit an existing student’s information
![alt text](images/image-7.png)
It is an empty page for now.

## 5. Forms
### Add a student
1. Create `forms.py` under `students` app folder, add the `StudentForm` class with all the fields of student.
```python
# students/forms.py
from django import forms

class StudentForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    date_of_birth = forms.DateField()
    enrollment_date = forms.DateField()
    grade = forms.IntegerField(min_value=1, max_value=12)

```
2. Update `views.py`
```py
# students/views.py
'''Add a new student'''
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
    context = {
        'form': StudentForm(),
        }
    return render(request, 'students/add.html', context)
```
3. Update `add.html` template.
```html
<!-- students/templates/students/add.html-->

{% extends "base.html" %}
{% block page_title %}
    <h2>Add a new student</h2>
{% endblock page_title %}

{% block page_content %}
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit" class="btn btn-primary">Submit</button>
    </form>
{% endblock page_content %}
```

Now the page for adding students looks:

![alt text](images/add_student.png)

### Edit information of an existing student
1. Update views.py
```py
'''Edit an existing student'''
def students_edit(request, student_id):
    student = Student.objects.get(id=student_id)
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
    context = {
        'student': student,
        'form': StudentForm(initial={
            'first_name': student.first_name,
            'last_name': student.last_name,
            'email': student.email,
            'date_of_birth': student.date_of_birth,
            'enrollment_date': student.enrollment_date,
            'grade': student.grade,
        }),
    }
    return render(request, 'students/edit.html', context)
```
2. Update edit.html template

Add the following code to `edit.html`
```html
{% block page_content %}
    {% block student %}
    <form method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit" class="btn btn-primary">Submit</button>
    </form>
    {% endblock student %}
{% endblock page_content %}
```

Now we can edit the information of an existing student.
插入视频：
### Validation for email

### Validation for grades

## 6. User Authentication
In this project, I use Django’s built-in authentication views and decorators to restrict access to authenticated users.
Here I encountered a problem because I did not know how to implement user authentication using Django. I asked ChatGPT for help.
### Set up the authentication system
First, ensure that Django's authentication systme is included in my project settings. It should be configured in `settings.py` by default.
Check `settings.py` to ensure:
```py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    # other installed apps...
]
```
### Create Login/Logout views
- views: Django provides built-in views for login and logout.
- urls: We still need to include routes for urls to use Django's built-in authentication views.
```python
urlpatterns = [
    # other URL patterns...
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
```
- templates: Create a `login.html` under `templates/registration` directory. Because by default, Django will look for the `login.html` file under `templates/registration` directory.

Now navigate to `http://localhost:8000/students/login/`, we will see the login page:
![alt text](images/login1.png)

### Restrict access using
To ensure only authenticated users can operate student records, I need to restrict access to views by using Django’s built-in `@login_required` decorator.

In `views.py`, I apply the `@login_required` decorator to functions which should only be accessed by authenticated users: add, edit and delete students. 
```python
# other imports...
from django.contrib.auth.decorators import login_required

'''Add a new student'''
@login_required
def students_add(request):
    ...

'''Edit an existing student'''
@login_required
def students_edit(request, student_id):
    ...

'''Delete a existing student'''
@login_required
def students_delete(request, student_id):
    ...
```

### Redirect users
After login, users will be redirected to the home page. After logout, users will be redirected to login page. Specify where users will be redirected in `settings.py`.
```python
LOGIN_REDIRECT_URL = '/students/'  # After login, users will be redirected to the home page
LOGOUT_REDIRECT_URL = '/login/'     # After logout, users will be redirected to login
```

### Add user login/logout button on each page
#### Change `base.html`
#### Problem
I get HTTP error code 405 (解释一下意思) at first. After debugging and reading documents, I realized that Django's built-in LogoutView requires a POST method by default.
Therefore I wrap the logout button in a **form** that submits via POST instead of using anchor tag via GET method.
