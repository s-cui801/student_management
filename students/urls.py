from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.students_list, name="students_list"),
    path("detail/<int:student_id>/", views.students_detail, name="students_detail"),
    path("add/", views.students_add, name="students_add"),
    path("edit/<int:student_id>/", views.students_edit, name="students_edit"),
    path("delete/<int:student_id>/", views.students_delete, name="students_delete"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]