from django.urls import path

from emobilis_crud.apps.students.views import student_list_view, student_input_view, student_update_view

app_name = "students"
urlpatterns = [
    path("list/", view=student_list_view, name="list"),
    path("input/", view=student_input_view, name="input"),
    path("update/<str:id>/", view=student_update_view, name="update"),
]
