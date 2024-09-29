from django.urls import path
from . import views

urlpatterns = [
    path("", views.students_list, name="students_list"),
    path("detail/<int:student_id>/", views.students_detail, name="students_detail"),
    path("add/", views.students_add, name="students_add"),
    path("edit/<int:student_id>/", views.students_edit, name="students_edit"),
]