from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, ListView, UpdateView

from emobilis_crud.apps.students.models import Student


class StudentListView(ListView):
    model = Student
    queryset = Student.objects.all()


student_list_view = StudentListView.as_view()


class StudentInputView(CreateView):
    model = Student
    fields = [
        "name",
        "email",
        "image",
    ]
    success_message = _("Information successfully saved")
    success_url = reverse_lazy('students:list')


student_input_view = StudentInputView.as_view()


class StudentUpdateView(UpdateView):
    model = Student
    fields = [
        "name",
        "email",
        "image",
    ]
    success_message = _("Information successfully saved")
    success_url = reverse_lazy('students:list')


student_update_view = StudentUpdateView.as_view()
